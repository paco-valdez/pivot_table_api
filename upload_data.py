import argparse
import pandas as pd
import boto3
from utils import read_config
from models.data import Dataset
from api import db, app


def main(args):
    dataset = read_config('pivots.json')
    config = read_config('config.json')
    bucket = boto3.resource('s3').Bucket(config['S3_BUCKET_DATASETS'])

    types = {}
    df = pd.read_csv(args.input_file)
    for t, columns in types.iteritems():
        if t in ('int64', 'float64'):
            for c in columns:
                df[c] = df[c].replace({99999: None})

    df['STAT_PROFILE_DATE_MONTH'] = df.apply(lambda row: '%s-%s' % (row['STAT_PROFILE_DATE_YEAR'],
                                                                    str(row['MONTHS']).zfill(2)),
                                             axis=1)
    for c in dataset['columns']:
        for r in dataset['rows']:
            if r == c:
                continue
            for func, values in dataset['values'].iteritems():
                for v in values:
                    key = '-'.join([func, v, r, c])
                    print(key)
                    df2 = df[[r, c, v]].reset_index()
                    df2[v].fillna(0, inplace=True)
                    res = getattr(df2.groupby([r, c]), func)().reset_index().pivot(index=r, columns=c, values=v)
                    res.reset_index(level=0, inplace=True)
                    res.fillna(0, inplace=True)
                    d = Dataset(key=key, data=res.to_dict(orient='split'), row=r, column=c, value=v, func=func)
                    db.session.add(d)
                    bucket.put_object(Key='%s.csv' % (key,), Body=res.to_csv(), ACL='public-read')
    db.session.commit()
    print('Success')

if __name__ == '__main__':
    # python upload_data.py finalapi.csv
    parser = argparse.ArgumentParser(description="Upload data file to server.")
    parser.add_argument('input_file', type=argparse.FileType('rb'))
    with app.app_context():
        main(parser.parse_args())

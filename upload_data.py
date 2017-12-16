import argparse
import pandas as pd
from utils import read_config
from models.data import Dataset
from api import db, app


def main(args):
    pivots = read_config('pivots.json')
    types = {}
    df = pd.read_csv(args.input_file)
    dtypes = df.columns.to_series().groupby(df.dtypes).groups
    for k in dtypes:
        names = []
        for t in dtypes[k]:
            names.append(str(t))
        types[str(k)] = names
    dataset = {
        'dataset': args.dataset_name,
        'types': types,
    }
    dataset.update(pivots)
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
                    # res[func + '_ALL'] = getattr(res, func)(axis=1)
                    d = Dataset(key=key, data=res.to_dict(orient='split'), row=r, column=c, value=v, func=func)
                    db.session.add(d)
    db.session.commit()
    print('Success')

if __name__ == '__main__':
    # python upload_data.py finalapi.csv finalapi
    parser = argparse.ArgumentParser(description="Upload data file to server.")
    parser.add_argument('input_file', type=argparse.FileType('rb'))
    parser.add_argument('dataset_name', type=str)
    with app.app_context():
        main(parser.parse_args())

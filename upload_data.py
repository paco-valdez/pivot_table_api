import boto3
import argparse


def main(args):
    client = boto3.resource(
        's3',
        aws_access_key_id='AKIAIB3LSJRSL5PBMZPQ',
        aws_secret_access_key='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',
    )
    client.Bucket('datasets-hruncx1gi').put_object(Key='%s.csv' % (args.dataset_name,), Body=args.input_file)
    print('Success')

if __name__ == '__main__':
    # python upload_data.py finalapi.csv finalapi
    parser = argparse.ArgumentParser(description="Upload data file to server.")
    parser.add_argument('input_file', type=argparse.FileType('rb'))
    parser.add_argument('dataset_name', type=str)
    main(parser.parse_args())

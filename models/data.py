import pandas as pd
import boto3
import io


DATASETS = ['finalapi']
dataframes = {}


client = boto3.client(
    's3',
    aws_access_key_id='AKIAIB3LSJRSL5PBMZPQ',
    aws_secret_access_key='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',
)
for key in DATASETS:
    obj = client.get_object(Bucket='datasets-hruncx1gi', Key='%s.csv' % (key,))
    dataframes[key] = pd.read_csv(io.BytesIO(obj['Body'].read()))


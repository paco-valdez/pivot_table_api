from flask_restful import Resource
from models.data import dataframes, DATASETS
from . import auth


class Dataset(Resource):
    @auth.login_required
    def get(self, dataset):
        if dataset not in DATASETS:
            return {'status': 'error', 'message': 'Dataset doesn\'t exists'}, 400
        df = dataframes[dataset]
        types = {}
        dtypes = df.columns.to_series().groupby(df.dtypes).groups
        for k in dtypes:
            names = []
            for t in dtypes[k]:
                names.append(str(t))
            types[str(k)] = names
        return {'types': types}

from flask_restful import Resource
from models.data import Dataset
from . import auth
from utils import read_config


pivots = read_config('pivots.json')


class DatasetResource(Resource):
    @auth.login_required
    def get(self, dataset):
        d = Dataset.query.filter_by(key=dataset)
        if not d:
            return {'status': 'error', 'message': 'Dataset doesn\'t exists'}, 400
        return d[0].to_dict()


class Spec(Resource):
    @auth.login_required
    def get(self):
        return pivots

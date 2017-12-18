from flask import Flask
from flask_restful import Api
from models import db
from resources.data import DatasetResource, Spec
from resources.users import Token, UserResource, UserList
from utils import read_config


config = read_config('config.json')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

api.add_resource(DatasetResource, '/dataset/<string:dataset>')
api.add_resource(UserList, '/user')
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(Token, '/token')
api.add_resource(Spec, '/spec')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,X-Requested-With,Access-Control-Request-Headers')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True)

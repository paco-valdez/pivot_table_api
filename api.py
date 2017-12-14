from flask import Flask
from flask_restful import Api
from models import db
from resources.data import Dataset
from resources.users import Token, UserResource, UserList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://api:demo2017@api.cfb60dbmbycz.us-west-1.rds.amazonaws.com/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

api.add_resource(Dataset, '/dataset/<string:dataset>')
api.add_resource(UserList, '/user')
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(Token, '/token')

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

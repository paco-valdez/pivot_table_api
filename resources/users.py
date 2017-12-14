from flask import g
from flask_restful import Resource, reqparse
from utils import str_max_length
from . import auth
from models import db
from models.user import User


class Token(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return {'token': token.decode('ascii')}


class UserResource(Resource):
    @auth.login_required
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'status': 'error', 'message': 'User doesn\'t exists'}, 400
        return {'username': user.username}


class UserList(Resource):
    # @auth.login_required  # Should check for admin permissions
    def post(self):
        args = self._post_parser().parse_args()
        username = args['username']
        password = args['password']
        if username is None or password is None:
            return {'status': 'error', 'message': 'Must provide a Username and a Password'}, 400
        if User.query.filter_by(username=username).first() is not None:
            return {'status': 'error', 'message': 'Username already exists'}, 400
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return {'status': 'success', 'message': 'User created'}, 201

    # noinspection PyMethodMayBeStatic
    def _post_parser(self):
        parser = reqparse.RequestParser(bundle_errors=True).copy()
        parser.add_argument("username", type=str_max_length(40), required=True)
        parser.add_argument("password", type=str_max_length(40), required=True)  # TODO: add a password strength check
        return parser

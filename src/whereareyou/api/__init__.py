from flask import Blueprint

from flask_rest_jsonapi import Api

from .users import UserList, UserDetail
from .authentication import UserRegister


json_api = Blueprint('api_prefix', __name__, url_prefix='/api/v1')
api = Api(blueprint=json_api)
api.route(UserList, 'user_list', '/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>')
api.route(UserRegister, 'user_register_list', '/singup')

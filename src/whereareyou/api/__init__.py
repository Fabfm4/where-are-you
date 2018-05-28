from flask import Blueprint

from flask_rest_jsonapi import Api

from .user import UserList, UserDetail


json_api = Blueprint('api_prefix', __name__, url_prefix='/api/v1')
api = Api(blueprint=json_api)
api.route(UserList, 'user_list', '/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>')

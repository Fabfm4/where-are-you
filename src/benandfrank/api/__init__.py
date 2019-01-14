# -*- coding: utf-8 -*-
from flask import Blueprint

from flask_rest_jsonapi import Api

from .users import UserList, UserDetail, MeResource, UserTypeDetail, UserTypeList
from .admin.keys_access import KeyAccessList, KeyAccessDetail


json_api = Blueprint('api_prefix', __name__, url_prefix='/api/v1')
api = Api(blueprint=json_api)
api.route(UserList, 'user_list', '/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>')
api.route(UserTypeList, 'user_type_list', '/user-types')
api.route(UserTypeDetail, 'user_type_detail', '/user-types/<int:id>')
api.route(KeyAccessList, 'keys_access_list', '/keys-access')
api.route(KeyAccessDetail, 'keys_access_detail', '/keys-access/<int:id>')
api.route(MeResource, 'me', '/me')


# -*- coding: utf-8 -*-
from whereareyou.models.users import User
from whereareyou.schemas.users import UserSchema
from whereareyou.models import db
from flask_jwt import jwt_required
from whereareyou.core.mixins import ResourceDetailMixin
from whereareyou.core.authentication import jwt_required_custom
from whereareyou.api.users.validatorsUsers import UserCreateValidate
from flask_rest_jsonapi import ResourceDetail, ResourceList


class UserList(ResourceList):

    @jwt_required_custom(permission='users')
    def before_get(self, args, kwargs):
        print("entra")

    methods = ['GET']
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {'before_get': before_get}
    }


class UserDetail(ResourceDetail):

    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {'before_get_object': ResourceDetailMixin.before_get_object}
    }

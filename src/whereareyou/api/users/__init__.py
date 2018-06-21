# -*- coding: utf-8 -*-
from whereareyou.models.users import User
from whereareyou.schemas.users import UserSchema
from whereareyou.models import db
from whereareyou.core.mixins import ResourceDetailMixin
from whereareyou.core.authentication import jwt_required_custom
from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi.resource import Resource


class UserList(ResourceList):

    @jwt_required_custom(permission='users')
    def before_get(self, args, kwargs):
        pass

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


class MeResource(Resource):

    @jwt_required_custom()
    def get(self, *args, **kwargs):
        print("hola")

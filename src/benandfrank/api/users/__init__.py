# -*- coding: utf-8 -*-
from ...models.users import User, UserType
from ...schemas.users import UserSchema, UserTypeSchema
from ...models import db
from ...core.mixins import ResourceDetailMixin
from ...core.authentication import jwt_required_custom

from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi.resource import Resource
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.exc import NoResultFound


class UserList(ResourceList):

    @jwt_required_custom(permission='Administrador')
    def before_get(self, args, kwargs):
        pass

    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {
            'before_get': before_get
        }
    }


class UserDetail(ResourceDetail):

    @jwt_required_custom(permission='Administrador')
    def before_get(self, args, kwargs):
        pass

    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {
            'before_get_object': ResourceDetailMixin.before_get_object,
            'before_get': before_get
        }
    }


class UserTypeList(ResourceList):

    @jwt_required_custom(permission='Administrador')
    def before_get(self, args, kwargs):
        pass

    schema = UserTypeSchema
    data_layer = {
        'session': db.session,
        'model': UserType,
        'methods': {
            'before_get': before_get
        }
    }


class UserTypeDetail(ResourceDetail):

    @jwt_required_custom(permission='Administrador')
    def before_get(self, args, kwargs):
        pass

    schema = UserTypeSchema
    data_layer = {
        'session': db.session,
        'model': UserType,
        'methods': {
            'before_get_object': ResourceDetailMixin.before_get_object,
            'before_get': before_get
        }
    }


class MeResource(Resource):

    @jwt_required_custom()
    def get(self, *args, **kwargs):
        print("hola")

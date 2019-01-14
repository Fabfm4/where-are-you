# -*- coding: utf-8 -*-
from ...models import db
from ...schemas.admin.key_access import KeyAccessSchema
from ...core.mixins import ResourceDetailMixin

from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi.exceptions import InvalidField
from ...models import db
from ...models.keys import KeyAccess
from ...core.authentication import jwt_required_custom


class KeyAccessList(ResourceList):

    @jwt_required_custom("Administrador")
    def before_get(self, args, kwargs):
        pass

    @jwt_required_custom("Administrador")
    def before_post(self, args, kwargs, data=None):
        pass

    def before_create_object(self, data, view_kwargs):
        user = KeyAccess.query.filter_by(host=data['host']).first()
        if user:
            raise InvalidField(
                detail='Key Access with this email already exists',
                source={'pointer': '/data/attributes/host'},
                title="Validation error"
            )
        data['key'] = data['host']

    schema = KeyAccessSchema
    data_layer = {
        'session': db.session,
        'model': KeyAccess,
        'methods': {
            'before_get': before_get,
            'before_post': before_post,
            'before_create_object': before_create_object
        }
    }


class KeyAccessDetail(ResourceDetail):

    @jwt_required_custom("Administrador")
    def before_get(self, args, kwargs):
        pass

    schema = KeyAccessSchema
    data_layer = {
        'session': db.session,
        'model': KeyAccess,
        'methods': {
            'before_get_object': ResourceDetailMixin.before_get_object,
            'before_get': before_get,
        }
    }

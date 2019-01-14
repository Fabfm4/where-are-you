# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from ..utils.nested_custom import NestedCustom
from ..models.users import UserType


class UserTypeSchema(Schema):

    class Meta:
        type_ = 'user_type'
        self_view = 'api_prefix.user_type_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.user_type_list'

    id = fields.Integer(dump_only=True)
    nombre_tipo_usuario = fields.Str(required=True)


class UserSchema(Schema):

    class Meta:
        type_ = 'user'
        self_view = 'api_prefix.user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.user_list'

    id = fields.Integer(dump_only=True)
    email = fields.Str(required=True)
    user_type_id = NestedCustom(UserTypeSchema(), model=UserType)
#    user_type_id = fields.Relationship(schema=UserTypeSchema)
    is_active = fields.Boolean(required=False, default=True)

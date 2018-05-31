from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserRegisterSchema(Schema):

    class Meta:
        type_ = 'register'
        self_view_many = 'api_prefix.register_list'

    token = fields.Str()

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserSchema(Schema):

    class Meta:
        type_ = 'user'
        self_view = 'api_prefix.user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.user_list'

    id = fields.Integer(as_string=True, dump_only=True)
    email = fields.Str()

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


def create_object(self, data, view_kwargs):
    print(self)
    print(data)
    print(view_kwargs)


class UserRegisterSchema(Schema):

    class Meta:
        type_ = 'register'
        self_view = 'api_prefix.register_list'
        self_view_kwargs = {}

    email = fields.Email(required=True)
    password = fields.Str(required=False)

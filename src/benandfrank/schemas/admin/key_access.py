# -*- coding: utf-8 -*-
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class KeyAccessSchema(Schema):

    class Meta:
        type_ = 'key_access'
        self_view = 'api_prefix.keys_access_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'api_prefix.keys_access_list'

    id = fields.Integer(dump_only=True)
    host = fields.Str(required=True)
    key = fields.Str(required=False, dump_only=True)
    created = fields.DateTime(required=False)
    updated = fields.DateTime(required=False)

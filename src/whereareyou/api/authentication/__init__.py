# -*- coding: utf-8 -*-
from flask_rest_jsonapi import ResourceList
from whereareyou.core.authentication.register import (
    before_create_object, UserRegisterSchema
)
from whereareyou.models import db
from whereareyou.models.users import User


class UserRegister(ResourceList):

    methods = ['POST']
    schema = UserRegisterSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'methods': {'before_create_object': before_create_object}
    }

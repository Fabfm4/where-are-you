from flask_rest_jsonapi import ResourceList
from whereareyou.core.authentication.register import UserRegisterSchema, create_object
from whereareyou.models import models
from six import with_metaclass
from whereareyou.models.user import User
from flask_rest_jsonapi.decorators import check_method_requirements
from flask import request


class UserRegister(ResourceList):

    methods = ['POST']
    schema = UserRegisterSchema
    data_layer = {
        'session': models.db.session,
        'model': User,
        'methods': {'create_object': create_object}
    }

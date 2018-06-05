from whereareyou.models.user import User
from whereareyou.schemas.user import UserSchema
from whereareyou.models import models
from whereareyou.core.mixins import ResourceDetailMixin
from whereareyou.api.users.validatorsUsers import UserCreateValidate
from flask_rest_jsonapi import ResourceDetail, ResourceList


class UserList(ResourceList, UserCreateValidate):

    def before_post(self, *args, **kwargs):
        super(UserList, self).before_post_mixin(User, *args, **kwargs)

    methods = ['GET']
    schema = UserSchema
    data_layer = {
        'session': models.db.session,
        'model': User
    }


class UserDetail(ResourceDetail):

    schema = UserSchema
    data_layer = {
        'session': models.db.session,
        'model': User,
        'methods': {'before_get_object': ResourceDetailMixin.before_get_object}
    }

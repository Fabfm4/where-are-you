from whereareyou.models.user import User
from whereareyou.schemas.user import UserSchema
from whereareyou.models import models
from whereareyou.core.mixins import ResourceDetailMixin
from flask_rest_jsonapi import ResourceList


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': models.db.session,
        'model': User
    }


class UserDetail(ResourceDetailMixin):

    def __init__(self):
        super(UserDetail, self).__init__()

    def before_get_object(self, view_kwargs):
        super(UserDetail, self).before_get_object()

    schema = UserSchema
    data_layer = {
        'session': models.db.session,
        'model': User,
        'methods': {'before_get_object': before_get_object}
    }

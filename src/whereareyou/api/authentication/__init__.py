from flask_rest_jsonapi import ResourceList


class UserRegisterList(ResourceList, UserCreateValidate):

    def before_post(self, *args, **kwargs):
        super(UserList, self).before_post_mixin(User, *args, **kwargs)

    methods = ['GET', 'POST']
    schema = UserSchema
    data_layer = {
        'session': models.db.session,
        'model': User
    }

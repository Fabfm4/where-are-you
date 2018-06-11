# -*- coding: utf-8 -*-
from flask_jwt import JWT, _jwt_required, CONFIG_DEFAULTS, current_identity
from functools import wraps
from ...models.users import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if user.is_active and user.verify_password(password):
            return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id)


def check_user_has_permission(user, permission):
    if permission:
        print(user.profile.permissions)


def jwt_required_custom(realm=None, permission=None):
    """View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """
    def wrapper(fn, *args, **kwargs):
        @wraps(fn)
        def decorator(*args, **kwargs):
            _jwt_required(realm or CONFIG_DEFAULTS['JWT_DEFAULT_REALM'])
            check_user_has_permission(current_identity.first(), permission)
            return fn(*args, **kwargs)
        return decorator
    return wrapper


jwt = JWT(None, authenticate, identity)

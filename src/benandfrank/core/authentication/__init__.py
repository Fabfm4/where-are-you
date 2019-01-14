# -*- coding: utf-8 -*-
from flask_jwt import JWT, _jwt_required, CONFIG_DEFAULTS, current_identity, JWTError
from ...utils.jwt import JWTCustom
from functools import wraps
from ...models.users import (
    User,
    UserType
)
from flask import current_app


def authenticate(email, password):
    domain = email.split('@')
    if domain[1] in current_app.config.get('DOMAIN_CAN_ACCESS'):
        user = User.query.filter_by(email=email).first()
        if user:
            if user.is_active:
                return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id)


def check_user_has_permission(user, permission):
    permission = UserType.query.filter_by(nombre_tipo_usuario=permission).first()
    if not user:
        return False

    if permission:
        if user.user_type_id != permission.id:
            return False

    return True


def jwt_required_custom(realm=None, permission=None):
    """View decorator that requires a valid JWT token to be present in the request
    :param realm: an optional realm
    """
    def wrapper(fn, *args, **kwargs):
        @wraps(fn)
        def decorator(*args, **kwargs):
            _jwt_required(realm or CONFIG_DEFAULTS['JWT_DEFAULT_REALM'])
            if not check_user_has_permission(
                current_identity.first(), permission
            ):
                raise JWTError(
                    'Access denied', 'access denied', status_code=403
                )
            return fn(*args, **kwargs)
        return decorator
    return wrapper


jwt = JWTCustom(None, authenticate, identity)

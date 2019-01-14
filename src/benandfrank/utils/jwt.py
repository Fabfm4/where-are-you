from flask_jwt import JWT, JWTError, _jwt
from flask import request, current_app
from ..models.keys import KeyAccess

def _default_auth_request_handler():
    data = request.get_json()
    username = data.get(current_app.config.get('JWT_AUTH_USERNAME_KEY'), None)
    origin = data.get('origin', None)
    criterion = [username, origin, len(data) == 2]
    password = data.get(current_app.config.get('JWT_AUTH_PASSWORD_KEY'), None)
    if password:
        criterion = [username, origin, password, len(data) == 3]

    if not all(criterion):
        raise JWTError('Bad Request', 'Invalid credentials')

    key_access = KeyAccess.query.filter_by(host=origin).first()
    if not key_access:
        raise JWTError('Bad Request', 'Invalid credentials')

    identity = _jwt.authentication_callback(username, password)

    if identity:
        access_token = _jwt.jwt_encode_callback(identity)
        return _jwt.auth_response_callback(access_token, identity)
    else:
        raise JWTError('Bad Request', 'Invalid credentials')

class JWTCustom(JWT):

    def __init__(self, app=None, authentication_handler=None, identity_handler=None):
        super(JWTCustom, self).__init__(app,authentication_handler,identity_handler)
        self.auth_request_callback = _default_auth_request_handler

    def init_app(self, app):
        super(JWTCustom, self).init_app(app)

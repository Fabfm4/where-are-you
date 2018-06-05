from flask_jwt import JWT, current_identity
from whereareyou.models.user import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if user.is_active and user.verify_password(password):
            return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id)


jwt = JWT(None, authenticate, identity)

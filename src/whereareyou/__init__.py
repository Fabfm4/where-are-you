from flask import Blueprint, Flask, url_for

from .models import models
from .api import api
from .core.authentication import jwt


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('APP_CONFIG_FILE')
    models.db.init_app(app)
    models.bcrypt.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    return app


app = create_app()

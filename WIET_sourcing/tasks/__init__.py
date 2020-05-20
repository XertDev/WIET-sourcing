from WIET_sourcing.models import db
from flask import Flask


def create_app_huey():
    app = Flask('huey_app', instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('WIET_sourcing/tasks/config.py', silent=True)

    db.init_app(app)

    return app

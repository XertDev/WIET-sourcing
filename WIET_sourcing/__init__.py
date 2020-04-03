from flask import Flask
from flask_migrate import Migrate

from WIET_sourcing.models import db

migrate = Migrate()


def create_app(config=None):
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object('config')
	app.config.from_pyfile('config.py')

	db.init_app(app)
	migrate.init_app(app, db)

	return app

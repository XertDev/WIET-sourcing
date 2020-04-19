from flask import Flask
from flask_graphql import GraphQLView
from flask_migrate import Migrate

from WIET_sourcing.models import db
from schemes.schema import schema

migrate = Migrate()


def create_app(config=None):
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object('config')
	app.config.from_pyfile('config.py', silent=True)

	db.init_app(app)
	migrate.init_app(app, db)

	app.add_url_rule(
		'/graphql',
		view_func=GraphQLView.as_view(
			'graphql',
			schema=schema,
			graphiql=True,
		)
	)

	return app

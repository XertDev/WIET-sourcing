from flask import Flask
from flask_graphql import GraphQLView
from flask_migrate import Migrate

from flask_cors import CORS

from WIET_sourcing.models import db
from WIET_sourcing.schemes.schema import schema

from logging.config import dictConfig

from WIET_sourcing.service.auth import AuthorizationMiddleware

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

migrate = Migrate()


def create_app(config=None):
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object('config')
	app.config.from_pyfile('config.py', silent=True)

	CORS(app)
	db.init_app(app)
	migrate.init_app(app, db)

	app.add_url_rule(
		'/graphql',
		view_func=GraphQLView.as_view(
			'graphql',
			schema=schema,
			graphiql=True,
			middleware=[AuthorizationMiddleware()]
		)
	)

	return app

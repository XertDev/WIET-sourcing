from flask import Flask
from flask_graphql import GraphQLView
from flask_migrate import Migrate

from flask_admin import Admin
from flask_cors import CORS

from WIET_sourcing.admin.secured_model_view import SecuredModelView
from WIET_sourcing.models import db
from WIET_sourcing.models.user_profile import UserProfile
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

from flask_admin.contrib.sqla import ModelView

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
		)
	)

	# Admin panel configuration
	app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
	admin = Admin(app, name='WIET-sourcing admin', template_mode='bootstrap3')
	admin.add_view(SecuredModelView(UserProfile, db.session))

	return app

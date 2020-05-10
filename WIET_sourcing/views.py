from flask import render_template
from datetime import datetime

from WIET_sourcing.service.auth import get_logged_in_user


def register_views(app):
    app.context_processor(base_context)
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login', view_func=login)


def index():
    return render_template('index.html')


def login():
    return render_template('login.html')


def base_context():
    return {
        "now": datetime.now(),
        "current_user": get_logged_in_user()
    }

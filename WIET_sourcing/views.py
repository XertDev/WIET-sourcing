from flask import render_template, send_from_directory, current_app
from datetime import datetime

from WIET_sourcing.service.auth import get_logged_in_user


def register_views(app):
    app.context_processor(base_context)
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/user_data/<path:filename>/', view_func=get_user_data)


def index():
    return render_template('index.html')


def get_user_data(filename):
    return send_from_directory(current_app.user_data, filename)


def base_context():
    return {
        "now": datetime.now(),
        "current_user": get_logged_in_user()
    }

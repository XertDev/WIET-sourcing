import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                    'sqlite:///appdb.db')

KEY_SIGNING_SECRET = os.getenv("WIET_SIGNING_SECRET")
STATIC_FOLDER = "/static"
USER_DATA_FOLDER = "/user_data"

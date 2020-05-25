import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                    'sqlite:///' + os.path.join(basedir, 'WIET_sourcing/appdb.db'))

KEY_SIGNING_SECRET = os.getenv("WIET_SIGNING_SECRET",
                               'WIET-SIGNING-SECRET')

STATIC_FOLDER = "/static"
USER_DATA_FOLDER = "/user_data"


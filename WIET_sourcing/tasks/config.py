import os
from huey import RedisHuey, SqliteHuey

#  TODO: refactor getting path
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = '/'.join(basedir.split('/')[:-2])

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                    'sqlite:///' + os.path.join(basedir, 'WIET_sourcing/appdb.db'))

REDIS_URL = os.getenv('REDIS_URL')
SQLITE_PATH = "sqlite:///" + os.path.join(basedir, 'WIET_sourcing/appdb.db')
print(SQLITE_PATH)

huey = RedisHuey(url=REDIS_URL) if REDIS_URL is not None else SqliteHuey(SQLITE_PATH)

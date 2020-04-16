import enum
from datetime import datetime

from WIET_sourcing.models import db


class UserRole(enum.Enum):
	ADMIN = 'ADMIN'
	# TODO: more roles


class UserProfile(db.Model):
	__tablename__ = 'user_profile'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, nullable=False)
	role = db.Column(db.Enum(UserRole), nullable=False)
	accuracy = db.Column(db.Float, nullable=False)
	wiet_points = db.Column(db.Integer, nullable=False, default=0)
	creation_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now)

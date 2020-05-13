from datetime import datetime
from .ownEnum import Enum

from sqlalchemy.ext.hybrid import hybrid_property

from WIET_sourcing.models import db


class UserRole(Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    # TODO: possibly more (?)


class UserProfile(db.Model):
    __tablename__ = "user_profile"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    role = db.Column(db.String(128), nullable=False)
    accuracy = db.Column(db.Float, nullable=False)
    wiet_points = db.Column(db.Integer, nullable=False, default=0)
    creation_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now)

    @hybrid_property
    def answered_question_count(self):
        return len(self.answers)

    @hybrid_property
    def created_question_set_count(self):
        return len(self.question_sets)

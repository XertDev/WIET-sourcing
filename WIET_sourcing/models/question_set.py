from datetime import datetime
from .ownEnum import Enum

from sqlalchemy.ext.hybrid import hybrid_property

import WIET_sourcing.models.user_profile
from WIET_sourcing.models import db


class Category(Enum):
    PHOTO = "PHOTO"
    TEXT = "TEXT"
    # TODO: possibly more (?)


class QuestionSet(db.Model):
    __tablename__ = "question_set"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)
    details = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now)
    owner_id = db.Column(db.Integer, db.ForeignKey("user_profile.id"), nullable=False)
    close_date = db.Column(db.TIMESTAMP)

    owner_profile = db.relationship(
        "UserProfile", backref=db.backref("question_sets", lazy=True)
    )

    tags = db.relationship(
        "QuestionSetToTag", back_populates="question_set"
    )

    @hybrid_property
    def question_count(self):
        return len(self.questions)

    @hybrid_property
    def report_count(self):
        return len(self.reports)

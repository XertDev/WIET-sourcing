from datetime import datetime

from WIET_sourcing.models import db
import enum


class ReportType(enum.Enum):
    INAPPROPRIATE_CONTENT = 'INAPPROPRIATE_CONTENT'
    # TODO: probably need to make more types


class QuestionSetReport(db.Model):
    __tablename__ = 'question_set_report'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    question_set_id = db.Column(db.Integer, db.ForeignKey('question_set.id'), nullable=False)
    type = db.Column(db.Enum(ReportType))
    details = db.Column(db.String(255), nullable=False)
    creation_time = db.Column(db.TIMESTAMP, nullable=False,  default=datetime.now)

    question_set = db.relationship('QuestionSet', backref=db.backref('reports', lazy=True))
    user = db.relationship('UserProfile', backref=db.backref('reports_sent', lazy=True))

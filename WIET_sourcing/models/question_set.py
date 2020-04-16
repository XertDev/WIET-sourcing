from WIET_sourcing.models import db
import enum


class Category(enum.Enum):
    PHOTO = 'PHOTO'
    TEXT = 'TEXT'
    # TODO: possibly more (?)


class QuestionSet(db.Model):
    __tablename__ = 'question_set'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)
    details = db.Column(db.Text, nullable=False)
    category = db.Column(db.Enum(Category), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    close_date = db.Column(db.Integer, db.TIMESTAMP)

    owner_profile = db.relationship('UserProfile', backref=db.backref('question_sets', lazy=True))

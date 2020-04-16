from WIET_sourcing.models import db


class QuestionAnswer(db.Model):
    __tablename__ = 'question_answer'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    creation_time = db.Column(db.TIMESTAMP, nullable=False)

    question = db.relationship('Question', backref=db.backref('answers', lazy=True))
    user = db.relationship('UserProfile', backref=db.backref('answered_questions', lazy=True))

from WIET_sourcing.models import db


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_set_id = db.Column(
        db.Integer, db.ForeignKey("question_set.id"), nullable=False
    )
    payload = db.Column(db.JSON, nullable=False)

    question_set = db.relationship(
        "QuestionSet", backref=db.backref("questions", lazy=True)
    )

from WIET_sourcing.models import db

class QuestionSetTag(db.Model):
    __tablename__ = "question_set_tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    question_sets = db.relationship("QuestionSetToTag", back_populates="tag")



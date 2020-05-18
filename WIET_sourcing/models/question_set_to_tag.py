from WIET_sourcing.models import db
from enum import Enum


class TagDifficultyLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"
    # TODO: possibly more (?)


class QuestionSetToTag(db.Model):
    __tablename__ = "question_set_to_tag"
    question_set_id = db.Column(db.Integer, db.ForeignKey("question_set.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("question_set_tag.id"), primary_key=True)

    question_set = db.relationship("QuestionSet", back_populates="tags")
    tag = db.relationship("QuestionSetTag", back_populates="question_sets")

    difficulty_level = db.Column(db.String(32))



from WIET_sourcing.models import db
import enum
import WIET_sourcing.models.question_set


class PromotionType(enum.Enum):
    BASIC = 'BASIC'
    PREMIUM = 'PREMIUM'
    # TODO: possibly more (?)


class PromotionAction(db.Model):
    __tablename__ = 'promotion_action'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_set_id = db.Column(db.Integer, db.ForeignKey('question_set.id'), nullable=False)
    type = db.Column(db.Enum(PromotionType), nullable=False)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP)

    question_set = db.relationship('QuestionSet', backref=db.backref('promotion_actions', lazy=True))

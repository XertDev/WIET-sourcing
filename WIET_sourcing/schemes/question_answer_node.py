from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question_answer import QuestionAnswer


class QuestionAnswerNode(SQLAlchemyObjectType):
    class Meta:
        model = QuestionAnswer
        interface = (relay.Node,)
        exclude_fields = (
            "user_id",
            "question_id",
        )

from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question import Question


class QuestionNode(SQLAlchemyObjectType):
    class Meta:
        model = Question
        interface = (relay.Node,)
        exclude_fields = ("question_set_id",)

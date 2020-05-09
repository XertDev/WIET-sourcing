from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question_set import QuestionSet


class QuestionSetNode(SQLAlchemyObjectType):
    class Meta:
        model = QuestionSet
        interface = (relay.Node,)
        exclude_fields = ("owner_id",)

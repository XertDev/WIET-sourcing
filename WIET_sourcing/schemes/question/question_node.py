import graphene
from graphene import relay

from WIET_sourcing.models.question import Question
from WIET_sourcing.question_loader import question_loader_manager
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = Question
        interfaces = (relay.Node,)
        exclude_fields = ("id", "question_set_id", "payload", )

    question = graphene.Field(question_loader_manager.create_question_union_node())

    # noinspection PyMethodParameters
    def resolve_question(parent, info):
        return question_loader_manager.load_question(parent.payload)

from graphene import relay

from WIET_sourcing.models.question_answer import QuestionAnswer
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionAnswerNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = QuestionAnswer
        interfaces = (relay.Node,)
        exclude_fields = (
            "id",
            "user_id",
            "question_id",
        )

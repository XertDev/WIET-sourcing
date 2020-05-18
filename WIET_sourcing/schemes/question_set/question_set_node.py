from graphene import relay


from WIET_sourcing.models.question_set import QuestionSet
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionSetNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = QuestionSet
        interfaces = (relay.Node,)
        exclude_fields = ("id", "owner_id",)

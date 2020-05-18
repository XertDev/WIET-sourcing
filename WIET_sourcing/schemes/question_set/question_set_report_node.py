from graphene import relay


from WIET_sourcing.models.question_set_report import QuestionSetReport
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionSetReportNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = QuestionSetReport
        interfaces = (relay.Node,)
        excluded_fields = (
            "id",
            "user_id",
            "question_set_id",
        )

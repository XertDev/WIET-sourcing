import graphene
from graphene import relay

from WIET_sourcing.models.question_set_to_tag import QuestionSetToTag
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionSetTagNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = QuestionSetToTag
        interfaces = (relay.Node,)
        exclude_fields = ("question_set_id","tag_id", "tag", "question_set")

    tag_name = graphene.String()

    @staticmethod
    def resolve_tag_name(parent, info, context):
        return parent.tag.name

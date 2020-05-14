from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question import Question
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class QuestionNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = Question
        interfaces = (relay.Node,)
        exclude_fields = ("id", "question_set_id", "payload", )

from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.orm import Session

from WIET_sourcing.models.question_set import QuestionSet


class QuestionSetNode(SQLAlchemyObjectType):
    class Meta:
        model = QuestionSet
        interfaces = (relay.Node,)
        exclude_fields = ("id", "owner_id",)

    @classmethod
    def get_model_from_global_id(cls, global_id: str) -> Optional[QuestionSet]:
        node_data = graphene.relay.node.from_global_id(global_id)
        if node_data[0] != cls.__name__:
            return None

        return QuestionSet.query.get(node_data[1])

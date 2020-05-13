from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question_answer import QuestionAnswer


class QuestionAnswerNode(SQLAlchemyObjectType):
    class Meta:
        model = QuestionAnswer
        interfaces = (relay.Node,)
        exclude_fields = (
            "id",
            "user_id",
            "question_id",
        )

    @classmethod
    def get_model_from_global_id(cls, global_id: str) -> Optional[QuestionAnswer]:
        node_data = graphene.relay.node.from_global_id(global_id)
        if node_data[0] != cls.__name__:
            return None

        return QuestionAnswer.query.get(node_data[1])

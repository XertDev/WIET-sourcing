from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question_set_report import QuestionSetReport


class QuestionSetReportNode(SQLAlchemyObjectType):
    class Meta:
        model = QuestionSetReport
        interfaces = (relay.Node,)
        excluded_fields = (
            "id",
            "user_id",
            "question_set_id",
        )

    @classmethod
    def get_model_from_global_id(cls, global_id: str) -> Optional[QuestionSetReport]:
        node_data = graphene.relay.node.from_global_id(global_id)
        if node_data[0] != cls.__name__:
            return None

        return QuestionSetReport.query.get(node_data[1])

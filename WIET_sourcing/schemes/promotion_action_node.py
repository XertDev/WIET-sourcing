from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.promotion_action import PromotionAction


class PromotionActionNode(SQLAlchemyObjectType):
    class Meta:
        model = PromotionAction
        interfaces = (relay.Node,)
        exclude_fields = ("id", "question_set_id", )

    @classmethod
    def get_model_from_global_id(cls, global_id: str) -> Optional[PromotionAction]:
        node_data = graphene.relay.node.from_global_id(global_id)
        if node_data[0] != cls.__name__:
            return None

        return PromotionAction.query.get(node_data[1])

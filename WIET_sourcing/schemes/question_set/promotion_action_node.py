from graphene import relay

from WIET_sourcing.models.promotion_action import PromotionAction
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class PromotionActionNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = PromotionAction
        interfaces = (relay.Node,)
        exclude_fields = ("id", "question_set_id", )

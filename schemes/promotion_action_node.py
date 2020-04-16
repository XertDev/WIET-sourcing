from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.promotion_action import PromotionAction


class PromotionActionNode(SQLAlchemyObjectType):
	class Meta:
		model = PromotionAction
		interface = (relay.Node, )
		exclude_fields = ('question_set_id', )

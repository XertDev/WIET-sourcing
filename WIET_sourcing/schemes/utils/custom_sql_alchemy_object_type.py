from typing import Optional

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models import db


class CustomSQLAlchemyObjectType(SQLAlchemyObjectType):
	class Meta:
		abstract = True

	@classmethod
	def get_model_from_global_id(cls, global_id: str) -> Optional[db.Model]:
		node_data = graphene.relay.node.from_global_id(global_id)
		if node_data[0] != cls.__name__:
			return None

		return cls.Meta.model.query.get(node_data[1])

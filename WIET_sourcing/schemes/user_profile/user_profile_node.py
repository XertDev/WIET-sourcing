from typing import Optional

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.user_profile import UserProfile


class UserProfileNode(SQLAlchemyObjectType):
    class Meta:
        model = UserProfile
        interfaces = (relay.Node,)
        exclude_fields = ("id", )

    @classmethod
    def get_model_from_global_id(cls, global_id: str) -> Optional[UserProfile]:
        node_data = graphene.relay.node.from_global_id(global_id)
        if node_data[0] != cls.__name__:
            return None

        return UserProfile.query.get(node_data[1])

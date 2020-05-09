import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.user_profile import UserProfile


class UserProfileNode(SQLAlchemyObjectType):
    class Meta:
        model = UserProfile
        interface = (relay.Node,)

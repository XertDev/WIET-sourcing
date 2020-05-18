from graphene import relay

from WIET_sourcing.models.user_profile import UserProfile
from WIET_sourcing.schemes.utils.custom_sql_alchemy_object_type import CustomSQLAlchemyObjectType


class UserProfileNode(CustomSQLAlchemyObjectType):
    class Meta:
        model = UserProfile
        interfaces = (relay.Node,)
        exclude_fields = ("id", )

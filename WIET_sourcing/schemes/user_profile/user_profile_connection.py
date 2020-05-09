from graphene import relay
from graphene_sqlalchemy_filter import FilterSet

from WIET_sourcing.models.user_profile import UserProfile
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode


class UserProfileConnection(relay.Connection):
    class Meta:
        node = UserProfileNode


class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            "name": ["eq", "ne", "in", "like", "ilike"],
            "accuracy": [...],
            "wiet_points": [...],
            "creation_time": [...],
        }

import graphene
from graphql import ResolveInfo, GraphQLError

from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode
from WIET_sourcing.service.auth import get_logged_in_user


def resolve_me(parent, info: ResolveInfo) -> UserProfileNode:
	user = get_logged_in_user()
	if not user:
		raise GraphQLError("User not authorized")
	return user.user_profile


me_field = graphene.Field(
	UserProfileNode,
	resolver=resolve_me,
)

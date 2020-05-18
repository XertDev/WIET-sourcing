import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode
from WIET_sourcing.service.auth import get_logged_in_user, validate_password


class ChangePassword(graphene.Mutation):
	"""
	Mutation to change password of current user
	"""

	class Arguments:
		password = graphene.String(required=True, description="Password")

	user_profile = graphene.Field(UserProfileNode)

	@staticmethod
	def mutate(root, info, password):
		user = get_logged_in_user()
		if not validate_password(password):
			raise GraphQLError("Invalid password")
		user.set_password(password)
		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			raise GraphQLError("Failed to change password")

		return ChangePassword(user_profile=user.user_profile)

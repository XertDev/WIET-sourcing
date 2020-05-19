import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode
from WIET_sourcing.service import user_service


class ConfirmEmail(graphene.Mutation):
	"""
	Mutation to confirm email, takes as argument email to be confirmed
	"""

	class Arguments:
		email = graphene.String(required=True, description="Email")
		code = graphene.String(required=True, description="Confirmation code")


	user_profile = graphene.Field(UserProfileNode)

	@staticmethod
	def mutate(root, info, email, code):
		user = user_service.get_user_by_email(email)
		if not user or not user.check_code(code):
			raise GraphQLError("Invalid confirmation code")

		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			raise GraphQLError("Failed to confirm email")

		return ConfirmEmail(user_profile=user.user_profile)

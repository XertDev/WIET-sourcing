from typing import Optional

import graphene
from graphql import GraphQLError
from validate_email import validate_email

from WIET_sourcing.service import user_service


class SignUp(graphene.Mutation):
	"""
	Mutation to self sign up user
	"""
	class Arguments:
		name = graphene.String(required=True, description="User visible name")
		email = graphene.String(required=True)
		password = graphene.String(required=True)

	success = graphene.Boolean()

	def mutate(self, info, name, email, password):
		if not validate_email(email):
			return SignUp(success=False)

		user_profile_id: Optional[int] = user_service.create_user(name, email, password)
		if not user_profile_id:
			return SignUp(success=False)

		return SignUp(success=True)


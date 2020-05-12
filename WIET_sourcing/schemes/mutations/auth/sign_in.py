import graphene
from graphql import GraphQLError

from WIET_sourcing.service import user_service
from WIET_sourcing.service.auth import generate_user_token


class SignIn(graphene.Mutation):
	"""
	Mutation to sign in a user
	"""

	class Arguments:
		email = graphene.String(required=True, description="Email")
		password = graphene.String(required=True, description="Password")

	token = graphene.String()

	def mutate(self, info, email, password):
		user_acc = user_service.get_user_by_email(email)
		if not user_acc or not user_acc.check_password(password):
			raise GraphQLError("Invalid email or password")

		token = generate_user_token(user_acc)

		return SignIn(token=token)

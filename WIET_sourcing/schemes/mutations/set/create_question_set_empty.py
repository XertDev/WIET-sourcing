import graphene
from graphql import GraphQLError

from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user
from WIET_sourcing.service.question_set_service import create_question_set


class CreateQuestionSetEmpty(graphene.Mutation):
	"""
	Mutation to create empty question set
	"""

	class Arguments:
		name = graphene.String(required=True, description="Set name")
		details = graphene.String(required=True, description="Set details")

	question_set = graphene.Field(QuestionSetNode)

	@staticmethod
	def mutate(root, info, name, category, details):
		if len(name) < 5 or len(details) < 20:
			raise GraphQLError("Name or description invalid")

		user = get_logged_in_user()
		question_set = create_question_set(name, details, user.user_profile)
		if not question_set:
			raise GraphQLError("Failed to create empty set")

		return CreateQuestionSetEmpty(question_set=question_set)

import graphene
from graphql import GraphQLError

from WIET_sourcing.models.question_set import Category
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user
from WIET_sourcing.service.question_set_service import create_question_set


class CreateQuestionSetEmpty(graphene.Mutation):
	"""
	Mutation to create empty question set
	"""

	class Arguments:
		name = graphene.String(required=True, description="Set name")
		# todo: find workaround for duplicated enum
		category = graphene.String(required=True, description="Set category")
		details = graphene.String(required=True, description="Set details")

	question_set = graphene.Field(QuestionSetNode)

	def mutate(self, info, name, category, details):
		if len(name) < 5 or len(details) < 20:
			raise GraphQLError("Name or description invalid")

		if not Category.has_value(category):
			raise GraphQLError("Invalid category")

		user = get_logged_in_user()
		question_set = create_question_set(name, details, Category[category].value, user.user_profile)
		if not question_set:
			raise GraphQLError("Failed to create empty set")

		return CreateQuestionSetEmpty(question_set=question_set)

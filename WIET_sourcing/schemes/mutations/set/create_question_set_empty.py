import graphene
from graphql import GraphQLError

from WIET_sourcing.models.question_set import Category
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
		description = graphene.String(required=True, description="Set name")

	id = graphene.ID()

	def mutate(self, info, name, category, description):
		if len(name) < 5 or len(description) < 20:
			raise GraphQLError("Name or description invalid")

		if not Category.has_value(category):
			raise GraphQLError("Invalid category")

		user = get_logged_in_user()
		question_set = create_question_set(name, description, Category(category), user.user_profile)
		if not question_set:
			raise GraphQLError("Failed to create empty set")

		return CreateQuestionSetEmpty(id=question_set.id)

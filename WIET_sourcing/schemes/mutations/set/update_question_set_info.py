import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.models.question_set import Category
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user


class UpdateQuestionSetInfo(graphene.Mutation):
	"""
	Mutation to update question set info
	"""

	class Arguments:
		id = graphene.ID(required=True, description="Question Set to update ID")
		name = graphene.String(required=False, description="Set name")
		category = graphene.String(required=False, description="Set category")
		details = graphene.String(required=False, description="Set details")

	question_set = graphene.Field(QuestionSetNode)

	def mutate(self, info, id, **kwargs):
		question_set = QuestionSetNode.get_model_from_global_id(id)
		if not question_set:
			raise GraphQLError("Question set not exist")

		if question_set.owner_profile != get_logged_in_user().user_profile:
			raise GraphQLError("Permission Denied")

		if "name" in kwargs:
			name = kwargs["name"]
			if len(name) < 5:
				raise GraphQLError("Invalid name")
			question_set.name = name

		if "details" in kwargs:
			details = kwargs["details"]
			if len(details) < 20:
				raise GraphQLError("Invalid description")
			question_set.details = details

		if "category" in kwargs:
			category_str = kwargs["category"]
			if not Category.has_value(category_str):
				raise GraphQLError("Invalid category")
			question_set.category = Category[category_str]

		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			raise GraphQLError("Failed to update question set info")

		return UpdateQuestionSetInfo(question_set=question_set)

import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user


class UpdateQuestionSetInfo(graphene.Mutation):
	"""
	Mutation to update question set info
	"""

	class Arguments:
		node_id = graphene.ID(required=True, description="Question Set to update ID")
		name = graphene.String(required=False, description="Set name")
		details = graphene.String(required=False, description="Set details")

	question_set = graphene.Field(QuestionSetNode)

	@staticmethod
	def mutate(root, info, node_id, **kwargs):
		question_set = QuestionSetNode.get_model_from_global_id(node_id)
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

		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			raise GraphQLError("Failed to update question set info")

		return UpdateQuestionSetInfo(question_set=question_set)

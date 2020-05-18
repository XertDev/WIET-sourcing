from datetime import datetime

import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user


class CloseQuestionSet(graphene.Mutation):
	"""
	Mutation to close question set
	"""

	class Arguments:
		node_id = graphene.ID(required=True, description="Question Set to close ID")

	question_set = graphene.Field(QuestionSetNode)

	@staticmethod
	def mutate(root, info, node_id):
		question_set = QuestionSetNode.get_model_from_global_id(node_id)
		if not question_set:
			raise GraphQLError("Question set not exist")

		if question_set.owner_profile != get_logged_in_user().user_profile:
			raise GraphQLError("Permission Denied")

		question_set.close_date = datetime.now()

		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			raise GraphQLError("Failed to close question set")

		return CloseQuestionSet(question_set=question_set)

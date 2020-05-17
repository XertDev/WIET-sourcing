import graphene
from graphql import GraphQLError

from WIET_sourcing.service.question_service import create_question_answer


class CreateTextQuestionAnswer(graphene.Mutation):
	"""
	Mutation which add answer to te question
	"""
	class Arguments:
		question_node_id = graphene.ID(required=True, description="Question ID which we want to add answer to")
		answer_indices = graphene.List(graphene.Int, required=True, description="selected answers")

	success = graphene.Boolean()

	def mutate(self, question_node_id: graphene.ID, answer_indices: graphene.List(graphene.String), info):
		payload = {
			"answer_index": answer_indices
		}

		answer_id = create_question_answer(question_node_id, payload)

		if not answer_id:
			raise GraphQLError("Failed to create answer")

		return CreateTextQuestionAnswer(success=True)

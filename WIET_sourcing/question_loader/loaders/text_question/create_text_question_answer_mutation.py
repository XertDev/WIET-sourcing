import graphene
from graphql import GraphQLError
from WIET_sourcing.models.question import Question
from graphql_relay import from_global_id

from WIET_sourcing.service.question_service import create_question_answer


class CreateTextQuestionAnswer(graphene.Mutation):
	"""
	Mutation which add answer to te question
	"""
	class Arguments:
		question_node_id = graphene.ID(required=True, description="Question ID which we want to add answer to")
		answer_indices = graphene.List(graphene.Int, required=True, description="selected answers")

	success = graphene.Boolean()

	@staticmethod
	def mutate(root, info, question_node_id: graphene.ID, answer_indices: graphene.List(graphene.Int)):
		payload = {
			"answer_index": answer_indices
		}

		answer_id = create_question_answer(question_node_id, payload)

		if not answer_id:
			raise GraphQLError("Failed to create answer")


		_, question_id = from_global_id(question_node_id)
		question = Question.query.get(question_id)
		for answer_index in answer_indices:
			question.payload["submitted_answers"][answer_index] += 1
		question.question_set.to_update = True

		return CreateTextQuestionAnswer(success=True)

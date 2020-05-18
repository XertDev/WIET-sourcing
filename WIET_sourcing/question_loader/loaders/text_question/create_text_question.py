import graphene
from graphql import GraphQLError

from WIET_sourcing.service.question_service import create_question


class CreateTextQuestion(graphene.ClientIDMutation):
	"""
	Mutation which add text question with answers to choose
	"""
	class Input:
		question_set_node_id = graphene.ID(required=True, description="ID of set which the question should be add to")
		multi_answer = graphene.Boolean(required=True, description="user can specify multiple answers for question")
		question = graphene.String(required=True, description="Question phrase")
		answers = graphene.List(graphene.String, required=True, description="Available answers")

	@staticmethod
	def mutate_and_get_payload(root, info, question_set_node_id, multi_answer, question, answers):
		payload = {
			"typename": "text_question",
			"multi_answer": multi_answer,
			"question": question,
			"answers": answers
		}

		question_id = create_question(question_set_node_id, payload)
		if not question_id:
			raise GraphQLError("Failed to create question")

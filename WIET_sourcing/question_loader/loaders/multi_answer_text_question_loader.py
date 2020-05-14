from typing import Type

import graphene

from WIET_sourcing.question_loader.abstract_question_loader import AbstractQuestionLoader


class MultiAnswerTextQuestionNode(graphene.ObjectType):
	question = graphene.String()
	answers = graphene.List(graphene.String)


class MultiAnswerTextQuestionLoader(AbstractQuestionLoader):
	typename = "multi_answer_text_question"

	@staticmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		return MultiAnswerTextQuestionNode

	@staticmethod
	def load_node_from_json(json: dict) -> graphene.ObjectType:
		pass


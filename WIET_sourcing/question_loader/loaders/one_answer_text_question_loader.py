from typing import Type

import graphene

from WIET_sourcing.question_loader.abstract_question_loader import AbstractQuestionLoader


class OneAnswerTextQuestionNode(graphene.ObjectType):
	question = graphene.String()
	answers = graphene.List(graphene.String)


class OneAnswerTextQuestionLoader(AbstractQuestionLoader):
	typename = "one_answer_text_question"

	@staticmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		return OneAnswerTextQuestionNode

	@staticmethod
	def load_node_from_json(json: dict) -> graphene.ObjectType:
		pass


from typing import Type

import graphene

from WIET_sourcing.question_loader.abstract_question_loader import AbstractQuestionLoader
from WIET_sourcing.question_loader.loaders.text_question.text_question_node import TextQuestionNode


class TextQuestionLoader(AbstractQuestionLoader):
	typename = "text_question"

	@staticmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		return TextQuestionNode

	@staticmethod
	def load_node_from_json(payload: dict) -> graphene.ObjectType:
		node = TextQuestionNode()
		node.multi_answer = payload["multi_answer"]
		node.question = payload["question"]
		node.answers = payload["answers"]

		return node


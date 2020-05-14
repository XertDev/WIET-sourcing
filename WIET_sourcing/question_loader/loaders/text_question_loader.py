from typing import Type

import graphene

from WIET_sourcing.question_loader.abstract_question_loader import AbstractQuestionLoader


class TextQuestionNode(graphene.ObjectType):
	question = graphene.String()
	answers = graphene.List(graphene.String)


class TextQuestionLoader(AbstractQuestionLoader):
	typename = "text_question"

	@staticmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		return TextQuestionNode

	@staticmethod
	def load_node_from_json(payload: dict) -> graphene.ObjectType:
		node = TextQuestionNode()
		node.question = payload["question"]
		node.answers = payload["answers"]

		return node


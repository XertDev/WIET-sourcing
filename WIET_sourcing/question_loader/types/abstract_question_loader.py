from abc import ABC, abstractmethod
from typing import Type

import graphene


class AbstractQuestionLoader(ABC):

	typename: str

	def __init__(self, typename: str):
		self.typename = typename
		super().__init__()

	@staticmethod
	@abstractmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		pass

	@staticmethod
	@abstractmethod
	def load_node_from_json(json: dict) -> graphene.ObjectType:
		pass




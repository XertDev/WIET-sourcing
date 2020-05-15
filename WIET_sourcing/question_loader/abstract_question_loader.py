from abc import ABC, abstractmethod
from typing import Type

import graphene


class AbstractQuestionLoader(ABC):
	"""
	Question loader interface. Base class that each loader must inherit from.
	"""

	@staticmethod
	@abstractmethod
	def get_question_node_class() -> Type[graphene.ObjectType]:
		"""
		Method to acquire class of loaded question
		:return: Class of Question loaded by specific loader
		(which must also be a subclass of graphene.ObjectType)
		"""
		pass

	@staticmethod
	@abstractmethod
	def load_node_from_json(json: dict) -> graphene.ObjectType:
		"""
		Decode question from json
		:param json encoded question:
		:return: Question object
		"""
		pass




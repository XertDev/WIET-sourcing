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
	def get_create_mutation_node() -> Type[graphene.ObjectType]:
		"""
		Method to acquire create mutation for question
		:return: Class of mutation which create question specified by loader
		(which must also be a subclass of graphene.ObjectType)
		"""
		pass

	@staticmethod
	@abstractmethod
	def get_create_answer_mutation_node() -> Type[graphene.ObjectType]:
		"""
		Method to acquire create answer mutation for question
		:return: Class of mutation which create answer for question specified by loader
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

	@staticmethod
	@abstractmethod
	def get_typename() -> str:
		"""
		:return: question type name
		"""
		pass

	@abstractmethod
	@staticmethod
	def calculate_answers_convergence(question_payload: dict, answers_count: int) -> float:
		"""
		:return answers convergence as float from interval [0, 1]
		"""
		pass



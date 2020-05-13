import inspect
import pkgutil
from typing import List, Any, Dict, Type

import graphene

from WIET_sourcing.question_loader.abstract_question_loader import AbstractQuestionLoader


class QuestionLoaderManager:
	"""
	Manager of loaded question loaders.
	Upon creation, this class will read all plugins in loaders directory
	"""
	_loaders: Dict[str, Type[AbstractQuestionLoader]]
	loaders_package = "WIET_sourcing.question_loader.loaders"

	def __init__(self):
		self.reload_loaders()
		self._loaders = {}

	def reload_loaders(self) -> None:
		"""
		Reset list of loaded loaders. Load all available loaders from specified directory
		:return:
		"""
		self._loaders = {}
		imported_package = __import__(self.loaders_package)

		for _, loader_name, is_pkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + "."):
			if not is_pkg:
				loader_module = __import__(loader_name)
				cls_members = inspect.getmembers(loader_module, inspect.isclass)
				for (_, loader_class) in cls_members:
					if issubclass(loader_class, AbstractQuestionLoader) and (loader_class is not AbstractQuestionLoader):
						typename = loader_class.typename

						if typename in self._loaders.keys():
							raise RuntimeError("Duplicated loader! {}".format(typename))
						self._loaders[typename] = loader_class

	def get_supported_question_node_classes(self) -> List[Type[graphene.ObjectType]]:
		"""
		:return: all registered question classes
		"""
		return [loader.get_question_node_class() for loader in self._loaders.values()]

	def load_question(self, payload: dict) -> graphene.ObjectType:
		"""
		:param payload: question
		:return: graphene question object
		"""
		if "typename" not in payload:
			raise ValueError("No typename info in supplied json")

		if payload["typename"] not in self._loaders.keys():
			raise RuntimeError("Question type not supported")

		return self._loaders[payload["typename"]].load_node_from_json(payload)

	def is_question_type_supported(self, typename: str) -> bool:
		return typename in self._loaders.keys()

import inspect
import pkgutil
from importlib import import_module
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
	_loader_file = "loader"

	def __init__(self):
		self._loaders = {}
		self.reload_loaders()

	def reload_loaders(self) -> None:
		"""
		Reset list of loaded loaders. Load all available loaders from specified directory
		:return:
		"""
		self._loaders = {}
		imported_package = import_module(self.loaders_package)

		for _, loader_name, is_pkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + "."):
			if is_pkg:
				try:
					loader_module_package = import_module("{}.{}".format(loader_name, self._loader_file))
				except ModuleNotFoundError as e:
					print("Plugin does not contain loader file")
					continue

				cls_members = inspect.getmembers(loader_module_package, inspect.isclass)
				for (_, loader_class) in cls_members:
					if issubclass(loader_class, AbstractQuestionLoader) and (loader_class is not AbstractQuestionLoader):
						typename = loader_class.typename
						print("Loaded question plugin: {}".format(typename))

						if typename in self._loaders.keys():
							raise RuntimeError("Duplicated loader! {}".format(typename))
						self._loaders[typename] = loader_class

	def get_supported_question_node_classes(self) -> List[Type[graphene.ObjectType]]:
		"""
		:return: all registered question classes
		"""
		x = [loader.get_question_node_class() for loader in self._loaders.values()]
		return x

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

	def create_question_union_node(self) -> Type[graphene.Union]:
		meta = type("Meta", (object, ), {
			"types": self.get_supported_question_node_classes()
		})
		return type("QuestionUnion", (graphene.Union,), {
				"Meta": meta
			})

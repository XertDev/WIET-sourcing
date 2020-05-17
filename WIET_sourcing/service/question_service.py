import logging
from typing import Optional

import graphene
from graphql import GraphQLError
from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.models.question import Question
from WIET_sourcing.models.question_set import QuestionSet
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.service.auth import get_logged_in_user


def create_question(question_set_node_id: graphene.ID, payload: dict) -> Optional[graphene.ID]:
	question_set: QuestionSet = QuestionSetNode.get_model_from_global_id(question_set_node_id)
	if not question_set:
		return None

	if question_set.owner_profile != get_logged_in_user().user_profile:
		raise GraphQLError("Permission denied")

	question = Question()
	question.question_set = question_set
	question.payload = payload

	db.session.add(question)

	try:
		db.session.commit()
	except exc.SQLAlchemyError:
		logging.exception("Failed to create question")
		return None
	return question.id

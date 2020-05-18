import logging
from typing import Optional

import graphene
from graphql import GraphQLError
from graphql_relay import from_global_id
from sqlalchemy import exc, and_

from WIET_sourcing import db
from WIET_sourcing.models.question import Question
from WIET_sourcing.models.question_answer import QuestionAnswer
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


def create_question_answer(question_node_id: graphene.ID, payload: dict) -> Optional[graphene.ID]:
	_, question_id = from_global_id(question_node_id)

	user = get_logged_in_user()

	question_answer = QuestionAnswer.query.filter(
		and_(
			QuestionAnswer.question_id == question_id,
			QuestionAnswer.user_id == user.id
		)
	).first()

	if not question_answer:
		raise GraphQLError("User already answered for the question")

	question_answer = QuestionAnswer()
	question_answer.question_id = question_id
	question_answer.user = user
	question_answer.payload = payload

	db.session.add(question_answer)

	try:
		db.session.commit()
	except exc.SQLAlchemyError:
		logging.exception("Failed to create question")
		return None
	return question_answer.id

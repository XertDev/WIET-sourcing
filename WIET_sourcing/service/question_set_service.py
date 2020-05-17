from typing import Optional

import logging
from sqlalchemy import exc

from WIET_sourcing import UserProfile
from WIET_sourcing.models import db
from WIET_sourcing.models.question_set import QuestionSet, Category


def create_question_set(name: str, details: Optional[str], category: Category, owner: UserProfile):
	question_set = QuestionSet()
	question_set.name = name
	question_set.details = details
	question_set.category = category
	question_set.owner_profile = owner

	db.session.add(question_set)

	try:
		db.session.commit()
	except exc.SQLAlchemyError:
		logging.exception("Couldn't create question set")
		return None
	return question_set


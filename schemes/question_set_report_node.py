from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from WIET_sourcing.models.question_set_report import QuestionSetReport


class QuestionSetReportNode(SQLAlchemyObjectType):
	class Meta:
		model = QuestionSetReport
		interface = (relay.Node, )
		excluded_fields = ('user_id', 'question_set_id', )

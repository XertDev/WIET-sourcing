import graphene
from graphene_sqlalchemy_filter import FilterableConnectionField

from schemes.promotion_action_node import PromotionActionNode
from schemes.question_answer_node import QuestionAnswerNode
from schemes.question_node import QuestionNode
from schemes.question_set.question_set_connection import QuestionSetConnection, QuestionSetFilter
from schemes.question_set.question_set_node import QuestionSetNode
from schemes.question_set_report_node import QuestionSetReportNode
from schemes.user_profile.user_profile_connection import UserProfileConnection, UserProfileFilter
from schemes.user_profile.user_profile_node import UserProfileNode


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()
	user = graphene.relay.Node.Field(UserProfileNode)
	question_set = graphene.relay.Node.Field(QuestionSetNode)
	promotion_action = graphene.relay.Node.Field(PromotionActionNode)
	question_answer = graphene.relay.Node.Field(QuestionAnswerNode)
	question = graphene.relay.Node.Field(QuestionNode)
	question_set_report = graphene.relay.Node.Field(QuestionSetReportNode)

	all_question_sets = FilterableConnectionField(QuestionSetConnection, filters=QuestionSetFilter())
	all_users = FilterableConnectionField(UserProfileConnection, filters=UserProfileFilter())

schema = graphene.Schema(query=Query)

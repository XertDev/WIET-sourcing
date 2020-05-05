import graphene
from graphene_sqlalchemy_filter import FilterableConnectionField

from WIET_sourcing.schemes.mutations.sign_up import SignUp
from WIET_sourcing.schemes.promotion_action_node import PromotionActionNode
from WIET_sourcing.schemes.question_answer_node import QuestionAnswerNode
from WIET_sourcing.schemes.question_node import QuestionNode
from WIET_sourcing.schemes.question_set.question_set_connection import QuestionSetConnection, QuestionSetFilter
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.schemes.question_set_report_node import QuestionSetReportNode
from WIET_sourcing.schemes.user_profile.user_profile_connection import UserProfileConnection, UserProfileFilter
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode


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

class Mutation(graphene.ObjectType):
	sign_up = SignUp.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

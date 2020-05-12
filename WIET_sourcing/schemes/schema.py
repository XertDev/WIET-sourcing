import graphene
from graphene_sqlalchemy_filter import FilterableConnectionField

from WIET_sourcing.schemes.mutations.auth.change_password import ChangePassword
from WIET_sourcing.schemes.mutations.auth.refresh_sign_in import RefreshSignIn
from WIET_sourcing.schemes.mutations.set.close_question_set import CloseQuestionSet
from WIET_sourcing.schemes.mutations.set.create_question_set_empty import CreateQuestionSetEmpty
from WIET_sourcing.schemes.mutations.set.update_question_set_info import UpdateQuestionSetInfo
from WIET_sourcing.schemes.mutations.auth.sign_up import SignUp
from WIET_sourcing.schemes.mutations.auth.sign_in import SignIn
from WIET_sourcing.schemes.promotion_action_node import PromotionActionNode
from WIET_sourcing.schemes.queries.me import me_field
from WIET_sourcing.schemes.question_answer_node import QuestionAnswerNode
from WIET_sourcing.schemes.question_node import QuestionNode
from WIET_sourcing.schemes.question_set.question_set_connection import (
    QuestionSetConnection,
    QuestionSetFilter,
)
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode
from WIET_sourcing.schemes.question_set_report_node import QuestionSetReportNode
from WIET_sourcing.schemes.user_profile.user_profile_connection import (
    UserProfileConnection,
    UserProfileFilter,
)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    question_set = graphene.relay.Node.Field(QuestionSetNode)
    promotion_action = graphene.relay.Node.Field(PromotionActionNode)
    question_answer = graphene.relay.Node.Field(QuestionAnswerNode)
    question = graphene.relay.Node.Field(QuestionNode)
    question_set_report = graphene.relay.Node.Field(QuestionSetReportNode)

    all_question_sets = FilterableConnectionField(
        QuestionSetConnection, filters=QuestionSetFilter()
    )
    all_users = FilterableConnectionField(
        UserProfileConnection, filters=UserProfileFilter()
    )

    me = me_field


class Mutation(graphene.ObjectType):
    sign_up = SignUp.Field()
    sign_in = SignIn.Field()
    refresh_sign_in = RefreshSignIn.Field()

    change_password = ChangePassword.Field()

    create_question_set_empty = CreateQuestionSetEmpty.Field()
    update_question_set_info = UpdateQuestionSetInfo.Field()
    close_question_set = CloseQuestionSet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

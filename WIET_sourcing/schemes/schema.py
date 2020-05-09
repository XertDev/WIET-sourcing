import logging

import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField

from WIET_sourcing.schemes.mutations.sign_up import SignUp, SignIn
from WIET_sourcing.schemes.promotion_action_node import PromotionActionNode
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
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode
from WIET_sourcing.service.auth import get_logged_in_user


class MessageField(graphene.ObjectType):
    message = graphene.String()


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    users = graphene.List(UserProfileNode)

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

    def resolve_users(self, info):
        current_user = get_logged_in_user()
        logging.info("Currently logged in: {current_user.email}")
        query = UserProfileNode.get_query(info)
        return query.all()


class Mutation(graphene.ObjectType):
    sign_up = SignUp.Field()
    sign_in = SignIn.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

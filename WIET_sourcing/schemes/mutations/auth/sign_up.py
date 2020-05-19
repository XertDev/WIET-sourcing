from random import randint
from typing import Optional
import graphene
from graphql import GraphQLError
from validate_email import validate_email

from WIET_sourcing import UserProfile
from WIET_sourcing.schemes.user_profile.user_profile_node import UserProfileNode
from WIET_sourcing.service import user_service
from WIET_sourcing.service.mailing_service import send_confirmation_mail_to
from WIET_sourcing.service.auth import validate_password


class SignUp(graphene.Mutation):
    """
    Mutation to self sign up user
    """

    class Arguments:
        name = graphene.String(required=True, description="User visible name")
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user_profile = graphene.Field(UserProfileNode)

    @staticmethod
    def mutate(root, info, name, email, password):
        if not validate_email(email) or not validate_password(password):
            raise GraphQLError("Invalid email or password")

        code = str(randint(1000, 9999))
        user_profile: Optional[UserProfile] = user_service.create_user(name, email, password, code)
        send_confirmation_mail_to(email, name, code)
        if not user_profile:
            raise GraphQLError("Failed to create user")

        return SignUp(user_profile=user_profile)



from typing import Optional
import logging
import jwt
import graphene
from graphql import GraphQLError
from validate_email import validate_email
import datetime
import time
from flask import current_app
from uuid import uuid4

from WIET_sourcing.service import user_service


class SignUp(graphene.Mutation):
    """
    Mutation to self sign up user
    """

    class Arguments:
        name = graphene.String(required=True, description="User visible name")
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, name, email, password):
        if not validate_email(email):
            return SignUp(success=False)

        user_profile_id: Optional[int] = user_service.create_user(name, email, password)
        if not user_profile_id:
            return SignUp(success=False)

        return SignUp(success=True)


class SignIn(graphene.Mutation):
    """
    Mutation to sign in a user
    """

    class Arguments:
        email = graphene.String(required=True, description="Email")
        password = graphene.String(required=True, description="Password")

    success = graphene.Boolean()
    token = graphene.String()

    def mutate(self, info, email, password):
        user_acc = user_service.get_user_by_email(email)
        if not user_acc.check_password(password):
            return SignIn(success=False)

        # Set expiration for the token 5 minutes in the future, convert it to
        # unix timestamp as a convention
        now = datetime.datetime.now() + datetime.timedelta(minutes=5)
        exp = time.mktime(now.timetuple())
        encoded = jwt.encode(
            {"user_id": user_acc.user_id, "exp": exp, "jti": str(uuid4())},
            current_app.config["KEY_SIGNING_SECRET"],
            algorithm="HS256",
        )
        return SignIn(success=True, token=encoded.decode("UTF-8"))
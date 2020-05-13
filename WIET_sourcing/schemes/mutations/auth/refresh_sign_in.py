import graphene

from WIET_sourcing.service.auth import get_logged_in_user, generate_user_token


class RefreshSignIn(graphene.Mutation):
    """
    Mutation to refresh authentication token
    """

    class Arguments:
        pass

    token = graphene.String()

    def mutate(self, info):
        user_account = get_logged_in_user()

        token = generate_user_token(user_account)

        return RefreshSignIn(token=token)

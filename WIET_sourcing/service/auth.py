import logging
from typing import Optional

import jwt
from flask import request, current_app, g

from WIET_sourcing.models.user_account import UserAccount


def get_user_from_token(token) -> UserAccount:
    parsed = jwt.decode(token, current_app.config['KEY_SIGNING_SECRET'], algorithms=["HS256"])
    return UserAccount.query.get(parsed['user_id'])


def get_logged_in_user() -> Optional[UserAccount]:
    """
    Get the current logged in user from the context data
    """
    if 'logged_in_user' in g:
        return g.logged_in_user
    return None


class AuthorizationMiddleware:
    ALLOWED_PATHS = ('signUp', 'signIn', '__schema')

    def _validate_token(self):
        auth_token = request.headers.get('Authorization', 'Bearer ').split('Bearer')[1].strip()
        try:
            user_data = get_user_from_token(auth_token)
            if not user_data:
                raise ValueError("User not found")
            g.logged_in_user = user_data
        except Exception:
            logging.exception("Token was invalid or expired")
            raise jwt.InvalidTokenError("Token was invalid or expired. "
                                        "Please set 'Authorization: Bearer <token> in the headers'")

    def resolve(self, next, root, info, **args):
        if info.path[0] not in self.ALLOWED_PATHS and len(info.path) == 1:
            self._validate_token()
        return next(root, info, **args)

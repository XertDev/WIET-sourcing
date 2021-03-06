import logging
from typing import Optional

from sqlalchemy import exc

from WIET_sourcing.models import db
from WIET_sourcing.models.user_account import UserAccount
from WIET_sourcing.models.user_profile import UserProfile, UserRole


def create_user(name: str, email: str, password: str, code: str) -> Optional[int]:
    user_account = UserAccount.query.filter_by(email=email).first()
    if user_account:
        return None

    user_account = UserAccount()
    user_account.email = email
    user_account.set_password(password)
    user_account.password_reset_tok = code

    user_profile = UserProfile()
    user_profile.name = name
    user_profile.role = UserRole.MEMBER.value
    user_profile.accuracy = 0
    user_profile.user_account = user_account

    db.session.add(user_account)
    try:
        db.session.commit()
        return user_profile
    except exc.SQLAlchemyError as e:
        logging.exception("Couldn't create profile")
    return None


def get_user_by_email(email: str) -> Optional[UserAccount]:
    return UserAccount.query.filter_by(email=email).first()

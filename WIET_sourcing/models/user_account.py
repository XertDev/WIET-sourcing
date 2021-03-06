from werkzeug.security import check_password_hash, generate_password_hash

from WIET_sourcing.models import db
from enum import Enum


class UserState(Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    # TODO: add more


class UserAccount(db.Model):
    __tablename__ = 'user_account'

    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), primary_key=True,  nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    password_reset_tok = db.Column(db.String(128))
    password_reset_exp = db.Column(db.TIMESTAMP)
    user_state = db.Column(db.String(32), nullable=False, server_default=UserState.UNVERIFIED.value)

    user_profile = db.relationship(
        "UserProfile", backref=db.backref("user_account", uselist=False)
    )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def check_code(self, code: str) -> bool:
        return self.password_reset_tok == code

    def set_email_as_verified(self) -> None:
        self.user_state = UserState.VERIFIED.value

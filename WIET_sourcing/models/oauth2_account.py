from WIET_sourcing.models import db


class OAuth2Account(db.Model):
    __tablename__ = "oauth2_account"

    client_id = db.Column(db.Integer, primary_key=True, nullable=False)
    client_secret = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.id"), nullable=False)
    provider = db.Column(db.Integer, nullable=False)

    user_profile = db.relationship(
        "UserProfile", backref=db.backref("user_profile", uselist=False)
    )

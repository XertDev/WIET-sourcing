from WIET_sourcing.models import db


class UserAccount(db.Model):
    __tablename__ = 'user_account'

    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), primary_key=True,  nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    password_reset_tok = db.Column(db.String(128))
    password_reset_exp = db.Column(db.TIMESTAMP)

    user_profile = db.relationship('UserProfile', backref=db.backref('user_profile', uselist=False))

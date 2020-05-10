import graphene

from WIET_sourcing.models import db
from WIET_sourcing.service.auth import get_logged_in_user, validate_password


class ChangePassword(graphene.Mutation):
	"""
	Mutation to change password of current user
	"""

	class Arguments:
		password = graphene.String(required=True, description="Password")

	success = graphene.Boolean()

	def mutate(self, info, password):
		user = get_logged_in_user()
		if not validate_password(password):
			return ChangePassword(success=False)
		user.set_password(password)
		db.session.commit()
		return ChangePassword(success=True)


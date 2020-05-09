from flask import request, url_for, redirect
from flask_admin.contrib import sqla

from WIET_sourcing.models.user_profile import UserRole
from WIET_sourcing.service.auth import get_logged_in_user


class SecuredModelView(sqla.ModelView):
	def is_accessible(self) -> bool:
		current_user = get_logged_in_user()
		if current_user is None:
			return False
		return current_user.user_profile.role == UserRole.ADMIN

	def inaccessible_callback(self, name, **kwargs) -> None:
		# redirect to login page if user doesn't have access
		return redirect(url_for('', next=request.url))

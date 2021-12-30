from functools import wraps

from flask_login import current_user
from flask import abort


def admin_only(function):
    """Make this page only accessible by the admin."""

    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id!=1:
            return abort(403)
        else:
            return function(*args, **kwargs)

    return decorated_function

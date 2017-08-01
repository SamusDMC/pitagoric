from flask import render_template, url_for, redirect, current_app

from ..decorators import auth
from ..helpers.token_helpers import remove_token_expired


# Functional route for control the user.
@auth.login_required
def user_profile(user):
    """
    Functinal route for rendering the user profile.
    """

    return render_template('profile.jinja')


# Functional route for log-out.
def logout():
    """
    Functional route for log-out the user.
    """

    return remove_token_expired()

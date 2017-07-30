from flask import render_template, url_for, redirect, current_app


# Functional view for control the user.
def user(user):
    return render_template('profile.jinja', user=user)


# Functional view for log-out.
def logout():
    redirect_to_login = redirect(url_for('login'))
    response = current_app.make_response(redirect_to_login)
    response.set_cookie('token', '', expires=0)

    return response

from flask import render_template, url_for, redirect, session


# Functional view for control the user.
def user(user=None):
    if 'username' in session:
        return render_template('profile.html', user=session['username'])
    else:
        return redirect(url_for('login'))


# Functional view for log-out.
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

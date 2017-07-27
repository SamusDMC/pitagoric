from flask import request, jsonify, session, abort
from ..models import User, db


def get_session():
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            user = db.session.query(User).filter_by(username=username).first()

            return jsonify(user.to_dict(['password']))
        else:
            abort(401)

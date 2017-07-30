from flask_via.routers.default import Functional

from user_service import *
from math_phrases import phrases

routes = [
    Functional('/users/<id>', user_by_id),
    Functional('/users', users),
    Functional('/user_session', user_session),
    Functional('/phrases', phrases)
]

from flask_via.routers.default import Functional, Pluggable, Blueprint
from user_service import *
from get_session import get_session

routes = [
    Functional('/get_session', get_session),
    Functional('/users/<id>', user_by_id),
    Functional('/users', users),
]

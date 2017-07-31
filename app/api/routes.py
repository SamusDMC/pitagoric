from flask_via.routers.default import Functional

from user_service import *
from math_phrases import phrases

routes = [
    Functional('/users/<id>', user_by_id),
    Functional('/current_user', current_user),
    Functional('/phrases', phrases),
]

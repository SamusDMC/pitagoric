from flask_via.routers.default import Functional, Pluggable, Blueprint
from user_service import *

routes = [
    Functional('/user/<id>', user_get_by_id),
    Functional('/user', user_get_all),
]

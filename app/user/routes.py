from flask_via.routers.default import Functional
from views import *

routes = [
    Functional('/<user>', user, endpoint='profile'),
    Functional('/logout', logout, endpoint='logout'),
]

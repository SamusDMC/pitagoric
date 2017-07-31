from flask_via.routers.default import Functional

from views import *

routes = [
    Functional('/<user>', user_profile, endpoint='profile'),
    Functional('/logout', logout, endpoint='logout'),
]

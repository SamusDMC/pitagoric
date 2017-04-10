from flask.ext.via.routers.default import Functional, Pluggable, Blueprint
from views import *

routes = [
    Functional('/', index),
    Pluggable('/login', LogIn, 'login'),
    Pluggable('/signup', SignUp, 'signup'),
    Blueprint('user', 'app.user', template_folder='templates', url_prefix='/user'),
]

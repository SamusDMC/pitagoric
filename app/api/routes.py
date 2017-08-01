from flask_via.routers.default import Functional

from user_service import *
from post_service import *
from post_category_service import *
from phrases_service import *

routes = [
    Functional('/user/<id>', user_by_id),
    Functional('/current_user', current_user),
    Functional('/phrases', phrases),
    Functional('/post/<id>', post_by_id),
    Functional('/posts', posts),
    Functional('/post_category/<id>', post_category_by_id),
    Functional('/post_categories', post_categories),
]

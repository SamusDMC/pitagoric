from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Model, relationship = db.Model, db.relationship
Column, ForeignKey = db.Column, db.ForeignKey
Integer, String, Date, BLOB = db.Integer, db.String, db.Date, db.BLOB
func, DateTime = db.func, db.DateTime


# The base model.
class BaseModel(Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)

    # Method to convert model to dictionary.
    def to_dict(self, hide=None):
        model_dict = {}
        columns = self.__table__.columns.keys()

        for key in columns:
            if not hide:
                model_dict[key] = getattr(self, key)
            else:
                if key not in hide:
                    model_dict[key] = getattr(self, key)

        return model_dict


class PostComment(BaseModel):
    comment = Column(String(600), nullable=False)
    date = Column(Date(), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def __init__(self, comment, date):
        self.comment = comment
        self.date = date


class Post(BaseModel):
    title = Column(String(100), nullable=False)
    date = Column(Date(), nullable=False)
    content = Column(BLOB(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_category_id = Column(Integer, ForeignKey('post_category.id'), nullable=False)
    comments = relationship(PostComment, backref='post', lazy='dynamic')

    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content


class PostCategory(BaseModel):
    name = Column(String(100), nullable=False)
    description = Column(String(150), nullable=False)
    posts = relationship(Post, backref='post_category', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description


class User(BaseModel):
    username = Column(String(100), unique=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(80))
    profile_image = Column(BLOB(1000))
    bio = Column(String(350))
    posts = relationship(Post, backref='user', lazy='dynamic')

    def __init__(self, fullname, username, email, password, profile_image, bio):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.profile_image = profile_image
        self.bio = bio

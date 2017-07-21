from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Model, relationship = db.Model, db.relationship
Column, ForeignKey = db.Column, db.ForeignKey
Integer, String, Date, BLOB = db.Integer, db.String, db.Date, db.BLOB


class Post(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date = Column(Date(), nullable=False)
    content = Column(BLOB(1000), nullable=False)
    # Relationship with `User`.
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # Relationship with `Post_Category`.
    post_category_id = Column(Integer, ForeignKey('post_category.id'), nullable=False)

    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content


class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(80))
    profile_image = Column(BLOB(1000))
    posts = relationship(Post, backref='user', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # Method for convert the model in an dict.
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }


class Post_Category(Model):
    __tablename__ = 'post_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(150), nullable=False)
    posts = relationship(Post, backref='post_category', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

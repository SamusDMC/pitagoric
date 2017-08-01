from faker import Factory
from faker.providers.misc import Provider

from app.models import *

faker = Factory.create()


def create_fake_user():
    """
    Function for create a fake user.
    """

    fullname = faker.name()
    username = faker.user_name()
    email = faker.email()
    password = Provider.password()
    profile_image = faker.image_url()
    bio = ''.join(faker.text(max_nb_chars=350, ext_word_list=None))
    fake_user = User(fullname, username, email, password, profile_image, bio)

    return fake_user


def create_fake_users(amount):
    """
    Function for create fake users.
    """

    fake_users = []

    for i in range(amount):
        fake_users.append(create_fake_user())

    return fake_users


def create_fake_post():
    """
    Function for create a fake post.
    """

    title = faker.text(max_nb_chars=100, ext_word_list=None)
    date = faker.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
    content = ''.join(faker.paragraphs(nb=8, ext_word_list=None))

    return Post(title, date, content)


def create_fake_posts(amount):
    """
    Function for create fake posts.
    """

    fake_posts = []

    for i in range(amount):
        fake_posts.append(create_fake_post())

    return fake_posts


def create_fake_post_comment():
    """
    Function for create a fake comment.
    """

    comment = faker.text(max_nb_chars=100, ext_word_list=None)
    date = faker.date_time_this_century(before_now=True, after_now=False, tzinfo=None)

    return PostComment(comment, date)


def create_fake_posts_comments(amount):
    """"
    Function for create fake comments.
    """

    fake_comments = []

    for i in range(amount):
        fake_comments.append(create_fake_post_comment())

    return fake_comments


def create_fake_post_category():
    """
    Function for create a fake category.
    """

    name = faker.text(max_nb_chars=50, ext_word_list=None)
    description = faker.text(max_nb_chars=150, ext_word_list=None)

    return PostCategory(name, description)


def create_fake_posts_categories(amount):
    """
    Function for create fake categories.
    """

    fake_categories = []

    for i in range(amount):
        fake_categories.append(create_fake_post_category())

    return fake_categories


def create_fake_data(db):
    """
    Function for create fake data.
    """

    # Creation of fake users.
    for fake_user in create_fake_users(10):
        # Creation of fake posts, post comments & post category.
        fake_post_category = create_fake_post_category()
        fake_posts = create_fake_posts(10)

        # Add comments to the posts.
        for fake_post in fake_posts:
            fake_post.comments = create_fake_posts_comments(5)

        # Add posts to the fake category.
        fake_post_category.posts = fake_posts
        # add posts to the fake user.
        fake_user.posts = fake_posts

        db.session.add(fake_user)
        db.session.add(fake_post_category)

    db.session.add(User(
        'Ricardo Moreno',
        'rich',
        'morenoricardo237@gmail.com',
        '1234',
        faker.image_url(),
        'Javascript & Python programmer.'
    ))

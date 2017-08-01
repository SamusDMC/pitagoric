from faker import Factory
from faker.providers.misc import Provider

from app.models import *

faker = Factory.create()


def fake_collection(fake_model, amount):
    """
    Function for create a fake collection.
    """

    fake_collection = []

    for i in range(amount):
        fake_collection.append(fake_model())

    return fake_collection


def fake_user():
    """
    Function for create a fake user.
    """

    fullname = faker.name()
    username = faker.user_name()
    email = faker.email()
    password = Provider.password()
    profile_image = faker.image_url()
    bio = ''.join(faker.text(max_nb_chars=350, ext_word_list=None))

    return User(fullname, username, email, password, profile_image, bio)


def fake_post():
    """
    Function for create a fake post.
    """

    title = faker.text(max_nb_chars=100, ext_word_list=None)
    date = faker.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
    content = ''.join(faker.paragraphs(nb=8, ext_word_list=None))

    return Post(title, date, content)


def fake_post_comment():
    """
    Function for create a fake comment.
    """

    comment = faker.text(max_nb_chars=100, ext_word_list=None)
    date = faker.date_time_this_century(before_now=True, after_now=False, tzinfo=None)

    return PostComment(comment, date)


def fake_post_category():
    """
    Function for create a fake category.
    """

    name = faker.word(ext_word_list=None)
    description = faker.text(max_nb_chars=150, ext_word_list=None)

    return PostCategory(name, description)


def create_fake_data(db):
    """
    Function for create fake data.
    """

    # Creation of fake users.
    for fake_user_dict in fake_collection(fake_user, 10):
        # Creation of fake posts, post comments & post category.
        fake_post_category_dict = fake_post_category()
        fake_posts_dict = fake_collection(fake_post, 10)

        # Add comments to the posts.
        for fake_post_dict in fake_posts_dict:
            fake_post_dict.comments = fake_collection(fake_post_comment, 5)

        # Add posts to the fake category.
        fake_post_category_dict.posts = fake_posts_dict
        # add posts to the fake user.
        fake_user_dict.posts = fake_posts_dict

        db.session.add(fake_user_dict)
        db.session.add(fake_post_category_dict)

    db.session.add(User(
        'Ricardo Moreno',
        'rich',
        'morenoricardo237@gmail.com',
        '1234',
        faker.image_url(),
        'Javascript & Python programmer.'
    ))

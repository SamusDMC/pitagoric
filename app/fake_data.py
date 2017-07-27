from faker import Factory
from faker.providers.misc import Provider
from models import *

fake = Factory.create()


# Creator for fake users.
def create_fake_user(amount=None):
    if amount:
        fake_users = []

        for i in range(0, amount):
            fullname = fake.name()
            username = fake.user_name()
            email = fake.email()
            password = Provider.password()
            bioTuple = fake.text(max_nb_chars=350, ext_word_list=None)
            profile_image = fake.image_url()
            bio = ''

            for line in bioTuple:
                bio += line

            fake_user = User(fullname, username, email, password, profile_image, bio)
            fake_users.append(fake_user)

        return fake_users
    else:
        fake_user = User(fake.name(), fake.email(), password())

        return fake_user


def create_fake_data(db):
    # Fake users.
    for fake_user in create_fake_user(10):
        db.session.add(fake_user)

    db.session.add(User('Ricardo Moreno', 'rich', 'morenoricardo237@gmail.com', '1234', fake.image_url(), 'Developer.'))

import unittest
from os import path, getenv

from flask_testing import TestCase

from app import create_app
from tests.test_helpers import create_fake_data
from app.models import db


class TestModels(TestCase):

    def create_app(self):
        BASE_DIR = path.abspath(path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(path.join(BASE_DIR, 'app.test.db'))

        app = create_app()
        app.config.update(SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI)

        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()

        if getenv('FAKE') != 'persist':
            db.drop_all()

    def testWithFakeData(self):
        create_fake_data(db)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()

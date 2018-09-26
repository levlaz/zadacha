import os
import unittest
import datetime

from flask.testing import FlaskClient
from zadacha.factory import create_app, db
from zadacha.models.user import User


class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def addUser(self):
        u = User(email='test@example.com', password='password', active=True, confirmed_at=datetime.datetime.utcnow())
        db.session.add(u)
        db.session.commit()
        return u

    def login(self, email, password):
        r = self.client.get('/auth/login')
        return self.client.post('/auth/login', data=dict(
            email = email,
            password = password,
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)
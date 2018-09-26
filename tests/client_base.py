import os
import unittest
import datetime

from zadacha.factory import create_app, db
from zadacha.models.user import User

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def addUser(self):
        u = User(email='test@example.com', password='password', confirmed_at=datetime.datetime.utcnow)
        db.session.add(u)
        db.session.commit()
        return u

    def login(self, email, password):
        return self.client.post('/auth/login', data=dict(
            email = email,
            password = password,
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)
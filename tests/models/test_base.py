import unittest

from datetime import datetime

from zadacha.factory import create_app, db
from zadacha.models.base import Base


class DummyModel(Base):
    """Dummy Non-Abstract Model for Testing Base Model"""
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    unique_label = db.Column(db.String, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)


class TestBaseModel(unittest.TestCase):


    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_init(self):
        b = Base()
        self.assertTrue(b.id is not None)


    def test_save(self):
        d = DummyModel(
                label='testing')
        self.assertTrue(d.id is None)
        d.save()
        self.assertTrue(d.id is not None)

        u = DummyModel(
                label='testing',
                unique_label='unique')
        u2 = DummyModel(
                label='testing',
                unique_label='unique')
        self.assertTrue(u.save())
        self.assertFalse(u2.save())


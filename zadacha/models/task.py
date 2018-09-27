from zadacha.factory import db
from zadacha.models.base import Base
from zadacha.models.user import User

class Task(Base):
    """ Task Model """
    title = db.Column(db.String(255))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def add_task(user, form):
        t = Task()
        t.title = form.title.data
        t.creator_id = user.id

        db.session.add(t)
        db.session.commit()

        return t
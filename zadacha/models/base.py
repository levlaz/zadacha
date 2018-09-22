from datetime import datetime
from sqlalchemy.exc import IntegrityError

from zadacha.factory import db


class Base(db.Model):
    """Base Class for Zadacha models"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def save(self):
        """Attempt to save a record

        Args:
            record - the record that we want to save

        Returns:
            True if successful

            False if IntegrityError is caught
        """
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False
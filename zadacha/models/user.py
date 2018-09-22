from werkzeug.security import generate_password_hash, check_password_hash

from zadacha.factory import db
from zadacha.models.base import Base


class User(Base):
    """User Model"""
    __tablename__ = "users"
    username = db.Column(db.String(256))
    email = db.Column(db.String(254), unique=True, index=True)
    password_hash = db.Column(db.String(256))


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha512')


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

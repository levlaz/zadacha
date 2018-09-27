import hashlib
import ldclient

from flask_security import UserMixin, RoleMixin

from zadacha.factory import db
from zadacha.models.base import Base

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(Base, RoleMixin):
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(Base, UserMixin):
    """User Model"""
    first_name = db.Column(db.String(254))
    last_name = db.Column(db.String(254))
    email = db.Column(db.String(254), unique=True, index=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(50))
    current_login_ip = db.Column(db.String(50))
    login_count = db.Column(db.Integer())

    roles = db.relationship('Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

    tasks = db.relationship('Task', backref='creator',
        lazy=True, cascade='all, delete-orphan')

    def get_user_hash(self):
        return hashlib.md5(self.email.encode()).hexdigest()

    def get_ld_user(self):
        user = {
            'key': self.get_user_hash(),
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'ip': self.current_login_ip,

            'custom': {
                'previous_login': self.last_login_at,
            },

            'privateAttributeNames': ['email']
        }

        return user

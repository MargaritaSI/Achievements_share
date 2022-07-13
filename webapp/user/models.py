from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash  # for password

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))  # from def set_password
    role = db.Column(db.String(10), index=True)  # admin or user

    def set_password(self, password):  #
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
        ''' True/false - compares encrypted password from database and password from user (encrypted leter with def set_password)'''

    @property  # decorator call method like an attribute/property without '()'
    def is_admin(self): # if admin - return True, other - false
        return self.role == 'admin'  # check for an administrator role

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)  # we could see name



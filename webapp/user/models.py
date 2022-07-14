from flask_login import UserMixin

from webapp.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):  # model=python class
    __tablename__ = 'users'  # creat spreadsheet

    id = db.Column(db.Integer, primary_key=True)  # creat columns
    username = db.Column(db.String)
    password = db.Column(db.String(120))  # with integers?
    email = db.Column(db.String(120), unique=True)
    telegram_username = db.Column(db.String(120))

    # method called when we display user instance in command line
    def __repr__(self):
        # we can see id + name.. of user for our understanding
        return (
            f"User {self.id}, {self.username}, {self.password}, "
            f"{self.email}, {self.telegram_username}"
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

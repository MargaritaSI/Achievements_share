from webapp.db import db


class User(db.Model):  # model=python class
    __tablename__ = 'users'  # creat spreadsheet

    id = db.Column(db.Integer, primary_key=True)  # creat columns
    username = db.Column(db.String)
    privilege = db.Column(db.String)
    urgency = db.Column(db.String)
    password = db.Column(db.String(120))  # with integers?
    todo_list = db.Column(db.String)
    name_business = db.Column(db.String)
    done = db.Column(db.String)
    not_done = db.Column(db.String)
    data_business = db.Column(db.Integer)
    # max len string + unic email
    email = db.Column(db.String(120), unique=True)
    telegram_username = db.Column(db.String(120), unique=True)

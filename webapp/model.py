from webapp.db import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String)
    disabled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return (f"News {self.id}, {self.title}, {self.url}"
                f"{self.published}, {self.disabled}")


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(500))
    priority = db.Column(db.Integer)
    description = db.Column(db.Text)
    due = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)
    shared = db.Column(db.Boolean)

    def __repr__(self):
        return (f"Task {self.id}, {self.user_id}, {self.name}"
                f"{self.priority}, {self.description}, {self.due_date}")


class User(db.Model):  # model=python class
    __tablename__ = 'users'  # creat spreadsheet

    id = db.Column(db.Integer, primary_key=True)  # creat columns
    username = db.Column(db.String)
    privilege = db.Column(db.String)
    urgency = db.Column(db.String)
    password = db.Column(db.String(4))  # with integers?
    todo_list = db.Column(db.String)
    name_business = db.Column(db.String)
    done = db.Column(db.String)
    not_done = db.Column(db.String)
    data_business = db.Column(db.Integer)
    # max len string + unic email
    email = db.Column(db.String(120), unique=True)

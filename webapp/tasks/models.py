from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from webapp.db import db


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), index=True
    )
    task = db.Column(db.String(500))
    priority = db.Column(db.Integer)
    due = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    completion_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime, default=func.now())
    shared = db.Column(db.Boolean, default=False)
    telegram = db.Column(db.Boolean, default=False)

    user = relationship('User', backref="tasks")
    comments = relationship('TaskComments', backref='task_comments')

    def __repr__(self):
        return f"Task {self.id}, {self.user_id}, {self.task}, " \
               f"{self.priority}, {self.due}, {self.completed}, " \
               f"{self.shared}, {self.telegram}"

    def comments_count(self):
        return TaskComments.query.filter(
            TaskComments.task_id == self.id
        ).count()


class TaskComments(db.Model):
    __tablename__ = 'task_comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    submitted_time = db.Column(db.DateTime, default=func.now())
    task_id = db.Column(
        db.Integer, db.ForeignKey('tasks.id', ondelete='CASCADE'), index=True
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), index=True
    )

    user = relationship('User', backref="users")
    task = relationship('Tasks', backref="tasks")

    def __repr__(self):
        return f"Task {self.id}, {self.task_id}, {self.user_id}, " \
               f"{self.submitted_time}, {self.comment}"

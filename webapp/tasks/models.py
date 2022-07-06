from webapp.db import db


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    task = db.Column(db.String(500))
    priority = db.Column(db.Integer)
    due = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    shared = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return (f"Task {self.id}, {self.user_id}, {self.task}, "
                f"{self.priority}, {self.due}, {self.completed}, "
                f"{self.shared}")

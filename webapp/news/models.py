from webapp import db


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

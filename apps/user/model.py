from exts import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_phone = db.Column(db.String(11), nullable=False, unique=True)
    user_email = db.Column(db.String(20))
    user_icon = db.Column(db.String(120))
    is_delete = db.Column(db.Boolean, default=False)
    ctime = db.Column(db.DateTime, default=datetime.now)
    article_rel = db.relationship("Article", backref="user")

    def __str__(self):
        return self.username

from exts import db
from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
    content = db.Column(db.Text, nullable=False)
    ctime = db.Column(db.DateTime, default=datetime.now)
    read_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    click_zan = db.Column(db.Integer, default=0)

    # 与用户表建立多对一的关系，用户为一，文章为多
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    astyle = db.Column(db.Integer, db.ForeignKey("article_style.id"), nullable=False, default=1)

    comment = db.relationship("Comment", backref="article_ref")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    ctime = db.Column(db.DateTime, default=datetime.now)


class ArticleStyle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    article = db.relationship("Article", backref="article_style_ref")

from flask import Blueprint, request, render_template, g, redirect, url_for

from apps.user.model import Users
from apps.article.model import Article
from exts import db

article_bp = Blueprint("article", __name__)


@article_bp.route("/art/article_publish", endpoint="add_art", methods=["GET", "POST"])
def article_publish():
    if request.method == "POST":
        title = request.form.get("art_title")
        content = request.form.get("content")
        art_user = request.form.get("art_user")
        print(art_user)
        article = Article()
        article.title = title
        article.content = content
        article.user_id = art_user
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("article.show", user_id=art_user))
    else:
        user_all = Users.query.filter(Users.is_delete == False).all()
        return render_template("article/add_article.html", users=user_all)


@article_bp.route("/art/article_show", endpoint="show", methods=["GET"])
def show_article():
    user_id = request.args.get("user_id")
    arts = Article.query.filter(Article.user_id == user_id).all()
    return render_template("article/show_article.html", arts=arts)

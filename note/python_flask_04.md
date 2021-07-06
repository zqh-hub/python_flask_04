##### Python_flask_04

###### 模型一对多

```python
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(12), nullable=False)
		......
    article_rel = db.relationship("Article", backref="user")   # 

    def __str__(self):
        return self.username
        
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
		......

    # 外键，与用户表建立多对一的关系，用户为一，文章为多
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
```

###### 模型多对多

```python
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) #外键，用户
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)#外键，文章
    comment = db.Column(db.String(255), nullable=False)
    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(12), nullable=False)
		......
    article_rel = db.relationship("Article", backref="user")
        
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
		......
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
```

###### flask- bootstrap

```
1、下载
pip install flask-bootstrap
2、创建
# exts/__init__
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
3、初始化app
# apps/__init__
from flask import Flask
from exts import db,bootstrap  # 引入
import settings


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app)
    bootstrap.init_app(app)  # 初始化
    return app
4、编写html
# base.html
{% extends "bootstrap/base.html" %}
{% block title %}Bootstrap{% endblock %}
{% block styles %}
    {{ super() }}
{% endblock %}
{% block navbar %}
    <ul class="nav nav-tabs">
        <li role="presentation" class="active"><a href="#">Home</a></li>
        <li role="presentation"><a href="#">Profile</a></li>
        <li role="presentation"><a href="#">Messages</a></li>
    </ul>
{% endblock %}

{% block content %}
    <h1>Hello, Bootstrap</h1>
{% endblock %}
```

###### cookie回话机制

```python
# app.py
@user_bp.route("/")
def index():
    uid = request.cookies.get("uid", None)    				# 判断是否有cookie
    if uid:
        user = Users.query.get(uid)
        return render_template("user/index.html", user=user)
    else:
        return render_template("user/index.html")

@user_bp.route("/login", methods=["GET", "POST"], endpoint="login")
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = Users.query.filter(Users.username == username).all()
        for user in users:
            flag = check_password_hash(user.password, password)
            if flag:
                response = redirect(url_for("user.index"))
                response.set_cookie("uid", str(user.id), max_age=1800)     		# 添加cookie
                return response
        else:
            return render_template("user/login.html", msg='用户名或密码有误')
    return render_template("user/login.html")


@user_bp.route("/logout", endpoint="logout")
def user_logout():
    response = redirect(url_for("user.index"))
    response.delete_cookie("uid")   					# 删除cookie
    return response

#base.html
<ul class="nav navbar-nav navbar-right">
{% if user %}										# 判断是否有user,有则证明已经登录
	<li class="dropdown">
		<a href="#" class="dropdown-toggle">欢迎 {{ user.username }}</a>
	</li>
{% else %}     											# 没有
		<li><a href="{{ url_for("user.login") }}">登录</a></li>
		<li><a href="{{ url_for("user.reg") }}">注册</a></li>
{% endif %}
</ul>
```

###### session机制

```python
# app.py
@user_bp.route("/")
def index():
    uid = session.get("uid")      								# 获取session
    if uid:
        user = Users.query.get(uid)
        return render_template("user/index.html", user=user)
    else:
        return render_template("user/index.html")

@user_bp.route("/login", methods=["GET", "POST"], endpoint="login")
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = Users.query.filter(Users.username == username).all()
        for user in users:
            flag = check_password_hash(user.password, password)
            if flag:
                response = redirect(url_for("user.index"))
                session["uid"] = user.id										# 设置session
                return response
        else:
            return render_template("user/login.html", msg='用户名或密码有误')
    return render_template("user/login.html")


@user_bp.route("/logout", endpoint="logout")
def user_logout():
    response = redirect(url_for("user.index"))
    # session.pop("uid")
    session.clear()													# 清空session
    return response
```


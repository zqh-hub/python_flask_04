from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.model import Users
from exts import db

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/")
def index():
    # uid = request.cookies.get("uid", None)    cookie 方式
    uid = session.get("uid")
    if uid:
        user = Users.query.get(uid)
        return render_template("user/index.html", user=user)
    else:
        return render_template("user/index.html")


@user_bp.route("/reg", methods=["GET", "POST"], endpoint="reg")
def user_register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        re_password = request.form.get("re_password")
        phone = request.form.get("phone")
        email = request.form.get("email")
        if password == re_password:
            user = Users()
            user.username = username
            user.password = generate_password_hash(password)
            user.user_phone = phone
            user.user_email = email
            db.session.add(user)
            db.session.commit()
            return render_template("user/login.html")
        else:
            msg = "密码与确认密码不一致"
            return render_template("user/register.html", msg=msg)
    return render_template("user/register.html")


@user_bp.route("/check_phone", endpoint="check_phone")
def check_phone_unique():
    phone = request.args.get("phone")
    user = Users.query.filter(Users.user_phone == phone).all()
    if user:
        return jsonify(code=1001, msg="手机号已经存在")
    else:
        return jsonify(code=200, msg="手机号码可使用")


@user_bp.route("/login", methods=["GET", "POST"], endpoint="login")
def user_login():
    if request.method == "POST":
        t = int(request.args.get("type"))
        if t == 1:
            username = request.form.get("username")
            password = request.form.get("password")
            users = Users.query.filter(Users.username == username).all()
            for user in users:
                flag = check_password_hash(user.password, password)
                if flag:
                    session["uid"] = user.id
                    return redirect(url_for("user.index"))
            else:
                return render_template("user/login.html", msg='用户名或密码有误')
        elif t == 2:
            pass
    return render_template("user/login.html")


@user_bp.route("/logout", endpoint="logout")
def user_logout():
    response = redirect(url_for("user.index"))
    # response.delete_cookie("uid")
    session.pop("uid")
    return response


@user_bp.route("/code", endpoint="send_code")
def phone_send_code():
    return "code"

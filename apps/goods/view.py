from flask import Blueprint, render_template, request

from apps.goods.model import Goods, UserLinkGoods
from apps.user.model import Users
from exts import db

goods_bp = Blueprint("goods", __name__)


@goods_bp.route("/goods/show", endpoint="gshow", methods=["GET"])
def goods_show():
    users = Users.query.filter(Goods.is_delete == False).all()
    goods = Goods.query.filter(Goods.is_delete == False).all()
    return render_template("goods/show.html", goods=goods, users=users)


@goods_bp.route("/goods/buy", endpoint="gbuy", methods=["GET"])
def goods_buy():
    goods_id = request.args.get("goods_id")
    print(goods_id)
    user_id = request.args.get("user_id")
    user_link_goods = UserLinkGoods()
    user_link_goods.user_id = user_id
    user_link_goods.goods_id = goods_id
    user_link_goods.num = 1
    db.session.add(user_link_goods)
    db.session.commit()
    return "购买成功"


@goods_bp.route("/goods/find_user", endpoint="find_user")
def find_user_by_goods():
    g_id = request.args.get("goods_id")
    gd = Goods.query.get(g_id)
    return render_template("goods/show_users_by_goods.html", goods=gd)


@goods_bp.route("/goods/find_goods", endpoint="find_goods")
def find_goods_by_user():
    user_id = request.args.get("user_id")
    user = Users.query.get(user_id)
    return render_template("goods/show_goods_by_users.html", user=user)

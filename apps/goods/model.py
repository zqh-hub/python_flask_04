from exts import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(12), default=100)
    is_delete = db.Column(db.Boolean, default=False)
    user = db.relationship("Users", backref="good_ref", secondary="user_link_goods")

    def __str__(self):
        return self.name


class UserLinkGoods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    goods_id = db.Column(db.Integer, db.ForeignKey("goods.id"), nullable=False)
    num = db.Column(db.Integer, default=1)

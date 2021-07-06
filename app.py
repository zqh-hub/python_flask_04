from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import create_app
from exts import db
from apps.user.model import Users
from apps.article.model import Article, Comment, ArticleStyle
from apps.goods.model import Goods, UserLinkGoods

app = create_app()
manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()

from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

# SQLALchemyをインスタンス化する
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # アプリのconfigを設定する
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=false,
        # SQL をコンソールログに出力する
        SQLALCHEMY_ECHO=True,
    )

    # SQLAlchemyとアプリを連携する
    db.init_app(app)

    # Migrateとアプリを連携する
    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app

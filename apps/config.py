from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfig クラスを作成する
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"

    # 画像アップロード先にapps/imagesを指定する
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))


# LocalConfig クラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# TestingConfig クラスを作成する
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


# config辞書にマッピングする
config = {"testing": TestingConfig, "local": LocalConfig}

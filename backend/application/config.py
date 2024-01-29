BASE_URL = 'http://127.0.0.1:8090'


class BaseConfig(object):
    SELECT_KEY = 'YUDREAM'
    JWT_SECRET_KEY = 'YUDREAM'
    DEBUG = False
    TESTING = False
    STATIC_FOLDER = './application/static'
    STATIC_URL_PATH = 'static'

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yd901455@localhost/mod_tweaker_gui'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

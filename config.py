class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""
    DB_NAME = "site.db"
    DB_USERNAME = "root"
    DB_PASSWORD = "test"
    ALLOWED_FILE_EXTENTIONS = ["OBS"]
    MAX_FILE_SIZE = 0.5 * 1024 * 1024


    UPLOADS = "/"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    ENV = 'production'
    pass

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    SESSION_COOKIE_SECURE = False

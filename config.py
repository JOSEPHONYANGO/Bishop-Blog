import os 

class Config:
    # SECRET_KEY = os.environ.get("joseph")
    SECRET_KEY = "joseph"
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog"

    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:papu@localhost/prudence"
    UPLOADED_PHOTOS_DEST = "app/static/img"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)


DEBUG = True

class TestConfig(Config):
    
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog_test"
    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:papu@localhost/prudence_test"

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog"
    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:papu@localhost/prudence"



config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}
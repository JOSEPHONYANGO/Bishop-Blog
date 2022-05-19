import os 

class Config:
<<<<<<< HEAD
    # SECRET_KEY = os.environ.get("joseph")
    SECRET_KEY = "joseph"
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog"

    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:noelle@localhost/prudence"
    UPLOADED_PHOTOS_DEST = "app/static/img"
=======
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://marknuchirimacharia:1OFFmark@localhost/myblog"
    UPLOADED_PHOTOS_DEST = "app/static/photos"
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
<<<<<<< HEAD
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog_test"
    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:noelle@localhost/prudence_test"

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog"
    SQLALCHEMY_DATABASE_URI = "postgresql://moringa:noelle@localhost/prudence"
=======
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://marknuchirimacharia:1OFFmark@localhost/myblog_test"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://marknuchirimacharia:1OFFmark@localhost/myblog"
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}
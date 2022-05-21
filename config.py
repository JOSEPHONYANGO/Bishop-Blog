import os 

class Config:
    # SECRET_KEY = os.environ.get("joseph")
    SECRET_KEY = "joseph"
    SQLALCHEMY_DATABASE_URI = "postgres://mngwklqowyirzk:b3d10ffbe6e35458e7a53364508aa3f49c8b14b8db020c05e816dfe3cff6a0ff@ec2-3-231-82-226.compute-1.amazonaws.com:5432/df0d1gf9vr6726"
    UPLOADED_PHOTOS_DEST = "app/static/img"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

     '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)


class TestConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog_test"
    # SQLALCHEMY_DATABASE_URI = "postgresql://moringa:papu@localhost/prudence_test"
    
class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:bishop@localhost/blog"
    # SQLALCHEMY_DATABASE_URI = "postgresql://moringa:papu@localhost/prudence"
    

    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_bootstrap import Bootstrap
# from flask_admin import Admin
from config import config_options

app = Flask(__name__)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
# photos = UploadSet("photos", IMAGES)
mail = Mail(app)
bootstrap = Bootstrap()
# admin = Admin()

def create_app(config_name):
    
    # app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    # admin.init_app(app)

    # Registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = "/authenticate")
    
    # Configure UploadSet
    # configure_uploads(app, photos)

    # return app
    # db.create_all()


    app.run(port=3003,host='0.0.0.0')

    def create_db():
        db.create_all()
        print ("Tables Created")

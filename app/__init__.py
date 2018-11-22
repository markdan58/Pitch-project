from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from flask_simplemde import SimpleMDE

# Initialaizing Flask extensions
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

# simple = SimpleMDE()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])
    


    # Initializing bootstrap
    bootstrap.init_app(app)

    # Initializing sqlalchemy database
    db.init_app(app)

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Initializing the login manager
    login_manager.init_app(app)


    # configure UploadSet
    configure_uploads(app,photos)

    #mail
    mail.init_app(app)


    return app

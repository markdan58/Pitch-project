
import os

class Config:
    '''
    This is the general configuration parent class
    '''

    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://danmark:5898danmark@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    '''
    This is the production configuration child class
    
    Args:
        Config: The parent configuration class with the general config settings
    '''
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://danmark:5898danmark@localhost/pitches_test'

class DevConfig(Config):
    '''
    Development configuration child class
    Arrgs:
        Config the parent configuration class with the general config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://danmark:5898danmark@localhost/pitches'


    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}
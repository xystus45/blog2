import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='makeangularleran'
    QUOTES_API_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://xystus:xystus@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch Website'
    SENDER_EMAIL = 'xystusngigi@gmail.com'

    


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://xystus:xystus@localhost/blog'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
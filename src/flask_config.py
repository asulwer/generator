class Config:
    #Base config
    SECRET_KEY = '!xFRSeWWR6#*4X9%VVD2'

class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    FLASK_ENV = 'production'
    
class DevConfig(Config):
    TESTING = False
    DEBUG = True
    FLASK_ENV = 'development'
    
class Config:
    DEBUG = True
    SERVER_NAME = 'localhost:10001'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
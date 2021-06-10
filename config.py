import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    '''
    Application config class


    Contains database location and settings, and auth key
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(
        BASE_DIR / 'sql' / 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'password'

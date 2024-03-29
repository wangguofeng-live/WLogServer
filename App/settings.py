import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_FOLDER = os.path.join(BASE_DIR,'templates')
STATIC_FOLDER = os.path.join(BASE_DIR,'static')

UPLOADS_FOLDER = os.path.join(BASE_DIR, 'uploads')

def get_upload_folder():
    return UPLOADS_FOLDER

def get_file_path(filename):
    return os.path.join(UPLOADS_FOLDER, filename)

def get_filename_suffix(filename):
    return os.path.splitext(filename)[1]

def get_filename_list():
    return os.listdir(UPLOADS_FOLDER)

def get_db_rul(dbinfo):

    ENGINE = dbinfo.get('ENGINE') or 'mysql'

    DRIVER = dbinfo.get('DRIVER') or 'pymysql'

    USER = dbinfo.get('USRE') or 'root'

    PASSWORD = dbinfo.get('PASSWORD') or '123456'

    HOST = dbinfo.get('HOST') or '127.0.0.1'

    PORT = dbinfo.get('PORT') or '3306'

    NAME = dbinfo.get('NAME') or 'test_db'

    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)

class Config:

    DEBUG = False

    TESTING = False

    SECRET_KEY = 'asdfaqer323423fdf3=='

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_PATH = UPLOADS_FOLDER


class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'FlaskDB_DEV'
    }

    SQLALCHEMY_DATABASE_URI = get_db_rul(DATABASE)


class TestingConfig(Config):

    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'FlaskDB_TEST'
    }

    SQLALCHEMY_DATABASE_URI = get_db_rul(DATABASE)

class StagingConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'FlaskDB_Stagin'
    }

    SQLALCHEMY_DATABASE_URI = get_db_rul(DATABASE)

class ProductConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'FlaskDB'
    }

    SQLALCHEMY_DATABASE_URI = get_db_rul(DATABASE)

envs = {
    'develop' : DevelopConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'product' : ProductConfig
}
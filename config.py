import os
import configparser

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MZK_IP = os.environ.get('MZK_IP', 'X.X.X.X:XXXX')
    TESTING = False
    DB_SERVER = 'mzk-postgres'
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}"
    
class ProductionConfig(Config):
    SRC_FOLDER = os.environ.get('SRC_FOLDER')
    DST_FOLDER = os.environ.get('DST_FOLDER') 
    DB_USER = '' #Production ready
    DB_PASSWORD = '' #Production ready
    DB_NAME = '' #Production ready
    SMB_PASSWORD = '' #Production ready
    SMB_USER = '' #Production ready

class DevelopmentConfig(Config):
    SRC_FOLDER = os.environ.get('SRC_FOLDER') or '/home/tran/Desktop/git/github/MichaelTran262/image-preparator/testFolder'
    DST_FOLDER = os.environ.get('DST_FOLDER') or '' # ADD MZK

    SMB_USER = os.environ.get('SMB_USER')
    SMB_PASSWORD = os.environ.get('SMB_PASSWORD')
    DB_USER = 'postgres'
    DB_PASSWORD = 'password'
    DB_NAME = 'baseddata'

class LocalDevelopmentConfig(DevelopmentConfig):
    DB_SERVER = 'localhost:5432'
    SMB_USER = 'tran'
    SMB_PASSWORD = 'M9mepemjin262'

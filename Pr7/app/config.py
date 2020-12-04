import os	

secret_key = "&LVKaB}fK(EqR"
PWD = os.path.abspath(os.curdir)	

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/users.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
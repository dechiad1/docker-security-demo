import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENALED = False
SECRET_KEY = 'dev-value'

#SQLALCHEMY_DATABASE_URI = 'postgresql://john:potato12@localhost/microblog'
SQLALCHEMY_DATABASE_URI = 'postgresql://john:potato12@172.17.0.2/microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

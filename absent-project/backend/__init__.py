from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "rmj_db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kersos'
    app.config['SQLALCHEMY_DATABASE_URI']=f'mysql://root@localhost:3307/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import Jemaat, Absen, Admin

    create_database(app)

    return app

def create_database(app):
    if not path.exists('backend/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created!')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routs import site
    
    app.register_blueprint(site)

    from .models import twitter_db

    create_database(app)

    return app

def create_database(app):
    db.create_all(app=app)

import os
from dotenv import load_dotenv


load_dotenv()

def init_app(app):
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['ASSETS_DEBUG'] = os.environ['FLASK_ENV'] != 'production'
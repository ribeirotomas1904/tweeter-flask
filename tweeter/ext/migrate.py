from flask_migrate import Migrate
from tweeter.ext.database import db


migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
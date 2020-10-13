from flask import Flask
from tweeter import views
from tweeter.ext import (
    configuration, database, commands, auth, debug, assets, migrate
)


def create_app():
    app = Flask(__name__)

    configuration.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    commands.init_app(app)
    auth.init_app(app)
    debug.init_app(app)
    views.init_app(app)
    assets.init_app(app)

    return app
from flask import redirect, url_for
from tweeter.views import auth, users


def init_app(app):
    @app.route('/')
    def home():
        return redirect(url_for('auth.register'))

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
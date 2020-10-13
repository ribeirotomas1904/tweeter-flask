from flask import redirect, url_for
from flask_login import current_user
from tweeter.views import auth, users, tweets


def init_app(app):

    @app.route('/')
    def home():
        if current_user.is_authenticated:
            return redirect(url_for('tweets.feed'))

        return redirect(url_for('tweets.explore'))


    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(tweets.bp)
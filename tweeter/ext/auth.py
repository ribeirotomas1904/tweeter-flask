from flask_login import LoginManager
from tweeter.models.user import User


login_manager = LoginManager()

def init_app(app):
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
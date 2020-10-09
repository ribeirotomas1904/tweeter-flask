from flask import Blueprint, render_template
from tweeter.models.user import User


bp = Blueprint('users', __name__)

@bp.route('/users/<username>')
def show(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/show.html', user=user)
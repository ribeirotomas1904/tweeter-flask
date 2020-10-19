from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from tweeter.models.user import User


bp = Blueprint('users', __name__)

@bp.route('/users/<username>')
def show(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/show.html', user=user)

@bp.route('/users/<username>/follow', methods=['POST'])
@login_required
def follow(username):
    return redirect(url_for('users.show', username=username))
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from tweeter.forms.tweets import CreateTweetForm
from tweeter.ext.database import db
from tweeter.models.tweet import Tweet


bp = Blueprint('tweets', __name__)

@bp.route('/feed', methods=['GET', 'POST'])
@login_required
def feed():
    form = CreateTweetForm()

    if request.method == 'POST' and form.validate_on_submit():
        tweet = Tweet(text=form.text.data)
        tweet.user = current_user 
        db.session.commit()

        return redirect(url_for('tweets.feed'))

    return render_template('tweets/feed.html', form=form, tweets=reversed(current_user.tweets))

@bp.route('/explore', methods=['GET', 'POST'])
def explore():
    return 'explore'
from datetime import datetime
from argon2 import PasswordHasher
from flask_login import UserMixin
from tweeter.ext.database import db
from tweeter.models.tweet import Tweet


ph = PasswordHasher()

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id')),
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    bio = db.Column(db.String(), nullable=True)
    picture_url = db.Column(db.String(), unique=True, nullable=True)
    banner_url = db.Column(db.String(), unique=True, nullable=True)
    tweets = db.relationship('Tweet', order_by='Tweet.created_at', backref='user', lazy=True)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(
        self,
        username,
        email,
        password,
        first_name,
        last_name,
    ):
        self.username = username
        self.email = email
        self.password = ph.hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.bio = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse iaculis pharetra risus, tristique gravida sem blandit ac.'
        # self.bio = None
        self.picture_url = None
        self.banner_url = None
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def followed_tweets(self):
        followerd = Tweet.query.join(
            followers, (followers.c.followed_id == Tweet.user_id)
        ).filter(
            followers.c.follower_id == self.id
        ).order_by(
            Tweet.created_at.desc()
        )
        onw = self.tweets
        return followed.union(onw).order_by(Tweet.created_at.desc())
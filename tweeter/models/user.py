from datetime import datetime
from argon2 import PasswordHasher
from flask_login import UserMixin
from tweeter.ext.database import db


ph = PasswordHasher()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(300), nullable=True)
    picture_url = db.Column(db.String(100), unique=True, nullable=True)
    banner_url = db.Column(db.String(100), unique=True, nullable=True)
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
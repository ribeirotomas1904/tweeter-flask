from datetime import datetime
from tweeter.ext.database import db


class Tweet(db.Model):
    __tablename__ = 'tweets'

    def __init__(self, text):
        self.text = text
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    text = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
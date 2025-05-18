from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text, nullable=False)
    author=db.Column(db.String(100), nullable=False)
    timestamp=db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.Text, nullable=False)
    author=db.Column(db.String(100), nullable=False)
    timestamp=db.Column(db.DateTime, default=datetime.utcnow)
    post_id=db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    parent_id=db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)

    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    parent = db.relationship('Comment', remote_side=[id], backref='replies')
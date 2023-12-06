from sqlalchemy import or_
from app.models import db, User, Post, Comment, follows, user_likes
from app import app

with app.app_context():
    user_1 = db.session.get(User, 1)
    print(user_1.posts)
    user_1.posts = []
    db.session.commit()

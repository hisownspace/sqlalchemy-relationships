from random import choice, randint
from sqlalchemy.sql import text
from app.models import db, User, Post


def seed_likes(users, posts):
    
    for user in users:
        num_likes = randint(0, 25)
        if num_likes < 10 or num_likes > 20:
            num_likes = randint(0, 20)
        for i in range(num_likes):
            post = choice(posts)
            if post not in user.likes:
                user.likes.append(post)
    
    for post in posts:
        num_likes = len(post.likes)
        if num_likes > 4:
            chance = max(6, 20-num_likes)
            for user in users:
                if randint(0,chance) < 3 and user not in post.likes:
                    post.likes.append(user)

    db.session.commit()


def undo_likes():
    db.session.execute(text("DELETE FROM user_likes;"))
    db.session.commit()

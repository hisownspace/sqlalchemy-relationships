from random import randint
from sqlalchemy.sql import text
from app.models import db, Post


def seed_posts(users):
    users = list(users.values())
    post_1 = {"content": "Insane gibberish!"}
    post_2 = {"content": "Empty rhetoric!"}
    post_3 = {"content": "Something about cats"}
    post_4 = {"content": "Controversial statement!"}
    post_5 = {"content": "Funny joke!"}
    post_6 = {"content": "Heartwarming story!"}
    post_7 = {"content": "Angry ranting!"}
    post_8 = {"content": "Thoughtful musings!"}

    posts = [post_1, post_2, post_3, post_4, post_5, post_6, post_7, post_8]
    posts_dic = {}
    for idx, post in enumerate(posts):
        this_post = Post(**post)
        posts_dic[f"post_{idx+1}"] = this_post
        while idx >= len(users) - 1:
            idx -= len(users)
        this_post.user = users[idx]
        for x in range(3):
            num = randint(0, len(users) - 1)
            if this_post.user is not users[num] and users[num] not in this_post.likes:
                this_post.likes.append(users[num])
            db.session.add(this_post)
        db.session.add(this_post)

    db.session.commit()
    return posts_dic


def undo_posts():
    db.session.execute(text("DELETE FROM posts;"))
    db.session.execute(text("DELETE FROM user_likes;"))
    db.session.commit()

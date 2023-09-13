from random import randint
from sqlalchemy.sql import text
from app.models import db, Post
from random import choice


def seed_posts(users):
    post_1 = "Insane gibberish!"
    post_2 = "Empty rhetoric!"
    post_3 = "Something about cats"
    post_4 = "Controversial statement!"
    post_5 = "Funny joke!"
    post_6 = "Heartwarming story!"
    post_7 = "Angry ranting!"
    post_8 = "Thoughtful musings!"
    post_9 = "Political garbage!"
    post_10 = "Random anecdote!"
    post_11 = "Plea for money!"
    post_12 = "Throwing someone under the bus!"
    post_12 = "Simping for a billionaire."
    post_13 = "Hating on a stranger!"
    post_14 = "Irrational Exuberance!"
    post_15 = "Unfunny joke!"
    

    posts = [   
                post_1,
                post_2,
                post_3,
                post_4,
                post_5,
                post_6,
                post_7,
                post_8,
                post_9,
                post_10,
                post_11,
                post_12,
                post_13,
                post_14,
                post_15
            ]


    for i in range(500):
        new_post = Post(content=choice(posts))
        new_post.user = choice(users)
        db.session.add(new_post)

    db.session.commit()
    return posts


def undo_posts():
    db.session.execute(text("DELETE FROM posts;"))
    db.session.execute(text("DELETE FROM user_likes;"))
    db.session.commit()

from sqlalchemy.sql import text
from app.models import db, Comment


def seed_comments(posts, users):
    user_1 = users["user_1"]
    user_2 = users["user_2"]

    post_1 = posts["post_1"]
    post_2 = posts["post_2"]
    post_3 = posts["post_3"]
    post_4 = posts["post_4"]
    # post_5 = posts["post_5"]
    # post_6 = posts["post_6"]
    # post_7 = posts["post_7"]
    # post_8 = posts["post_8"]

    comment_1 = Comment(user=user_1, post=post_1, content="Good point, man!!!")
    comment_2 = Comment(user=user_1, post=post_1, content="Good point, man!!!")
    comment_3 = Comment(user=user_1, post=post_1, content="Good point, man!!!")
    comment_4 = Comment(user=user_1, post=post_2, content="Good point, man!!!")
    comment_5 = Comment(user=user_1, post=post_2, content="Good point, man!!!")
    comment_6 = Comment(user=user_2, post=post_3, content="Good point, man!!!")
    comment_7 = Comment(user=user_2, post=post_3, content="Good point, man!!!")
    comment_8 = Comment(user=user_2, post=post_3, content="Good point, man!!!")
    comment_9 = Comment(user=user_2, post=post_4, content="Good point, man!!!")
    comment_10 = Comment(user=user_2, post=post_4, content="Good point, man!!!")
    comment_11 = Comment(user=user_2, post=post_4, content="Good point, man!!!")

    comments = [
        comment_1,
        comment_2,
        comment_3,
        comment_4,
        comment_5,
        comment_6,
        comment_7,
        comment_8,
        comment_9,
        comment_10,
        comment_11,
    ]

    [db.session.add(comment) for comment in comments]

    db.session.commit()


def undo_comments():
    db.session.execute(text("DELETE FROM comments;"))
    db.session.commit()

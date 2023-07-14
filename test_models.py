from sqlalchemy import or_
from app.models import db, User, Post, Comment, follows, user_likes
from app import app

with app.app_context():
    user_1 = User.query.get(1)
    post_1 = Post.query.get(1)
    post_2 = Post.query.get(2)
    user_2 = User.query.get(2)
    user_3 = User.query.get(3)
    post_3 = Post.query.get(4)
    comment_1 = Comment(content="That's a really good point!")
    comment_1.post = post_2
    comment_1.user = user_2
    # db.session.add(comment_1)
    latest_comment = db.session.get(Comment, (2, 2))
    legacy_comment = Comment.query.get([2, 2])
    # two_comments = db.session.get(Comment, ([2, 2], [3, 3]))
    two_comments = Comment.query.filter(
        or_(
            Comment.user_id == 2,
            Comment.user_id == 3,
        )
    ).all()
    print(latest_comment.user)
    print(legacy_comment.post)
    print(two_comments)

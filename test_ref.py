from sqlalchemy import or_
from app.models import db, User, Post, post_user_likes
from app import app

with app.app_context():
    # Get all posts from a single user
    user_1 = db.session.get(User, 1)
    # print(user_1.posts)
    print(user_1)

    # Create a new post and associate it with a user
    new_post = Post(content="This is my first post!")
    new_post.user = user_1
    # or
    # user.posts.append(new_post)
    db.session.add(new_post)
    db.session.commit()

    # Get top five most liked posts
    all_posts = Post.query.all()
    most_liked_posts = sorted(all_posts, key=lambda post: len(post.user_likes))[-5:]
    for post in most_liked_posts:
        print(
            f"{post.user.username} made the post '{post.content}', which had {len(post.user_likes)} likes!"
        )

    # Delete all posts by a user
    user_1.posts = []

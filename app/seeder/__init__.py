from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts
from .likes import seed_likes

# from .comments import seed_comments, undo_comments

seed_commands = AppGroup("reset")


def seed():
    users = seed_users()
    posts = seed_posts(users)
    likes = seed_likes(users, posts)
    # seed_comments(posts, users)


def undo():
    undo_posts()
    undo_users()
    # undo_comments()


@seed_commands.command("all")
def reset():
    undo()
    seed()

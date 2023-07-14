from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

# from .comments import seed_comments, undo_comments

seed_commands = AppGroup("reset")


# @seed_commands.command('all')
def seed():
    users = seed_users()
    posts = seed_posts(users)
    # seed_comments(posts, users)


# @seed_commands.command('undoes')
def undo():
    undo_users()
    undo_posts()
    # undo_comments()


@seed_commands.command("all")
def reset():
    undo()
    seed()

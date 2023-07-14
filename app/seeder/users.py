from app.models import db, User
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(username="Demo")
    marnie = User(username="marnie")
    bobbie = User(username="bobbie")
    admin = User(username="admin")

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(admin)

    db.session.commit()

    return {"user_1": demo, "user_2": marnie, "user_3": bobbie, "user_4": admin}


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute(text("DELETE FROM users;"))
    db.session.execute(text("DELETE FROM follows"))
    db.session.commit()

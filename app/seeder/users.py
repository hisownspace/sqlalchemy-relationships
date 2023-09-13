from app.models import db, User
from sqlalchemy.sql import text
from faker import Faker

fake = Faker()


# Adds a demo user, you can add other users here if you want
def seed_users():

    users = set()

    for i in range(100):
        user = fake.name().split(" ")[0]
        if "." not in user:
            users.add(User(username=user))

    for user in users:
        db.session.add(user)

    db.session.commit()

    return list(users)


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute(text("DELETE FROM users;"))
    db.session.execute(text("DELETE FROM follows"))
    db.session.commit()

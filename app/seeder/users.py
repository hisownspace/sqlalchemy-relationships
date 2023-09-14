from app.models import db, User
from sqlalchemy.sql import text
from faker import Faker

fake = Faker()


# Adds a demo user, you can add other users here if you want
def seed_users():

    usernames = set()

    for i in range(50):
        username = fake.name().split(" ")[0]
        if "." not in username:
            usernames.add(username)
    
    users = []

    for username in usernames:
        user = User(username=username)
        db.session.add(user)
        users.append(user)


    db.session.commit()

    return users


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute(text("DELETE FROM users;"))
    db.session.commit()

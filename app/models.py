from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

follows = db.Table(
    "follows",
    db.Column("follower", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("followed", db.Integer, db.ForeignKey("users.id"), primary_key=True),
)

user_likes = db.Table(
    "user_likes",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)

    # Relationships
    posts = db.relationship("Post", back_populates="user", cascade="delete-orphan, all")
    comments = db.relationship("Comment", back_populates="user")
    liked_posts = db.relationship(
        "Post",
        secondary="user_likes",
        back_populates="user_likes",
    )

    followers = db.relationship(
        "User",
        secondary="follows",
        # this user will be placed into this column
        primaryjoin=follows.columns.followed == id,
        # the other user will be placed into this column
        secondaryjoin=follows.columns.follower == id,
        # which is which doesn't technically matter, the follows column could
        # just be labeled a and b, for example, but make sure you're consistent
        # with backref, the other attribute is automatically created
        # backref="following",
        back_populates="following",
    )

    following = db.relationship(
        "User",
        secondary="follows",
        primaryjoin=follows.c.follower == id,
        secondaryjoin=follows.c.followed == id,
        back_populates="followers",
    )


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String(2000), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")
    user_likes = db.relationship(
        "User",
        secondary="user_likes",
        back_populates="liked_posts",
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.id,
            "user_likes": [user.id for user in self.user_likes],
        }


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    content = db.Column(db.String(2000))

    post = db.relationship("Post", back_populates="comments")
    user = db.relationship("User", back_populates="comments")

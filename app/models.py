from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
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

post_user_likes = db.Table(
    "post_user_likes",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)

    # Relationships

    posts = db.relationship("Post", back_populates="user")

    liked_posts = db.relationship(
        "Post",
        secondary="post_user_likes",
        back_populates="user_likes",
    )


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String(2000), nullable=False)

    # Relationships

    user = db.relationship("User", back_populates="posts")

    user_likes = db.relationship(
        "User", secondary="post_user_likes", back_populates="liked_posts"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.id,
            "user_likes": [user.id for user in self.user_likes],
        }

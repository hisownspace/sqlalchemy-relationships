from flask import Flask
from flask_migrate import Migrate
from app.config import Configuration

from app.models import db, User, Post
from app.seeder import seed_commands

app = Flask(__name__)

app.config.from_object(Configuration)

# Tell flask about our seed commands
app.cli.add_command(seed_commands)

db.init_app(app)
Migrate(app, db)

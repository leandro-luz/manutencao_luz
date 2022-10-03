import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), nullable=False, index=True, unique=True)
    password = db.Column(db.String(50))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        # formats what is shown in the shell when print is
        # called on it
        return '<User {}>'.format(self.username)


@app.route('/')
def home():
    result = "Hello World"
    return result


if __name__ == '__main__':
    app.run()

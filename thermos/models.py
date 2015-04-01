from datetime import datetime
from .thermos import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable= False)
    description = db.Column(db.String(300))

    def __repl__(self):
        return "<Bookmark '{}': '{}'>".format(self.description, self.url)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repl__(self):
        return "<User %r>" % self.username
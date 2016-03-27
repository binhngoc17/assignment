import datetime

from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


class User(db.Document):
    uid  = db.IntField(required=True)
    date = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(required=True)

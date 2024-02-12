from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    auth_provider = db.StringField(choices=('local', 'google', 'linkedin'), default='local')
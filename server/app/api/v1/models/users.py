"""User model for storing user related details in the database"""
import mongoengine as db

db.connect('morya', host='mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/')
class User(db.Document):
    user_id = db.SequenceField(primary_key=True)
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    hashed_password = db.StringField(required=True)
    profile_picture = db.StringField()
    subscription_status = db.StringField()
    authentication_provider = db.StringField(default='local')
    is_active = db.BooleanField(default=True)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "profile_picture": self.profile_picture,
            "subscription_status": self.subscription_status,
            "authentication_provider": self.authentication_provider,
            "is_active": self.is_active
        }

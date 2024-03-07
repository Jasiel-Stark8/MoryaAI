"""User model for storing user related details in the database"""
from ..database import db

class User(db.Document):
    """Define the user class model for storing user related details in the database"""
    user_id = db.SequenceField(primary_key=True)
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    hashed_password = db.StringField(required=True)
    profile_picture = db.StringField()
    subscription_status = db.StringField()
    authentication_provider = db.StringField(default='local')
    is_active = db.BooleanField(default=True)
    articles = db.ListField(db.ReferenceField('Article'))

    def to_json(self):
        """Initialize the user model with the required fields"""
        from .articles import Article
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
    

"""Article model for storing article related details in the database"""
from datetime import datetime
from ..database import db
from .published_content import Published


class Article(db.Document):
    user = db.ReferenceField('User', required=True)
    article_id = db.SequenceField(primary_key=True)
    title = db.StringField(required=True, unique=True)
    content = db.StringField(required=True)
    author = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    updated_at = db.DateTimeField(default=datetime.now)
    is_published = db.BooleanField(default=False)
    platform = db.ReferenceField(Published)

    def to_json(self):
        from .users import User
        return {
            "article_id": self.article_id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_published": self.is_published
        }

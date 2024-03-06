from datetime import datetime
from ..database import db

class Published(db.Document):
    """
    Represents a published content.

    Attributes:
        user (ReferenceField): The user who published the content.
        article (ReferenceField): The article that was published.
        published_id (SequenceField): The unique identifier for the published content.
        published_at (DateTimeField): The date and time when the content was published.
        published_by (ReferenceField): The user who published the content.
        platform (StringField): The platform on which the content was published.

    Methods:
        to_json: Converts the published content object to a JSON representation.
    """

    user = db.ReferenceField('User', required=True)
    article = db.ReferenceField('Article', required=True)
    published_id = db.SequenceField(primary_key=True)
    published_at = db.DateTimeField(default=datetime.now)
    published_by = db.ReferenceField('User', required=True)
    platform = db.StringField(default='web')

    def to_json(self):
        from .users import User
        from .articles import Article
        return {
            "published_id": self.published_id,
            "published_at": self.published_at,
            "published_by": self.published_by,
            "platform": self.platform
        }

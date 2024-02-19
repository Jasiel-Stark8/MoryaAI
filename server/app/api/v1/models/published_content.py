from datetime import datetime
import mongoengine as db
from users import User
from articles import Article
from platforms import Platform

db.connect('morya', host='mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/')

class Published(db.Document):
    article = db.ReferenceField(Article, required=True)
    published_id = db.SequenceField(primary_key=True)
    published_at = db.DateTimeField(default=datetime.now)
    published_by = db.ReferenceField(User, required=True)
    platform = db.StringField(default='web')

    def to_json(self):
        return {
            "published_id": self.published_id,
            "published_at": self.published_at,
            "published_by": self.published_by,
            "platform": self.platform
        }

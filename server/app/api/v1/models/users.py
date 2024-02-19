from mongoengine import connect, Document, StringField, EmailField, BooleanField

connect('morya', host='mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/')
class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    hashed_password = StringField(required=True)
    profile_picture = StringField()
    subscription_status = StringField()
    authentication_provider = StringField(default='local')
    is_active = BooleanField(default=True)

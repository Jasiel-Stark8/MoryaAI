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

print('Creating User...')
user = User(
    username='admin',
    email='admin@morya.com',
    hashed_password='admin',
    profile_picture='admin.png',
    subscription_status='active',
    authentication_provider='local',
    is_active=True
)
existing_user = User.objects(email=user.email).first()
if not existing_user:
    User.save(user)
else:
    print('User already exists')

print('Querying user')
user = User.objects(email='admin@morya.com').first()
print(user.to_json() if user else 'User not found')
print('Done.')

print('Updating User...')
User.objects(email='admin@morya.com').update_one(
    username='admina',
    hashed_password='admin100'
)

print('Updated username and password')
user = User.objects(email='admin@morya.com').first()
print(user.to_json() if user else 'User not found')

# ==============================================
print('Creating User 2...')
user = User(
    username='Morya',
    email='morayai@morya.com',
    hashed_password='morya120',
    profile_picture='morya.png',
    subscription_status='active',
    authentication_provider='google',
    is_active=True
)
existing_user = User.objects(email=user.email).first()
if not existing_user:
    User.save(user)
else:
    print('User already exists')
# ==============================================
# ==============================================
print('Creating User 3...')
user = User(
    username='Jason',
    email='Jason@morya.com',
    hashed_password='jason',
    profile_picture='jason.png',
    subscription_status='active',
    authentication_provider='linkedin',
    is_active=True
)
existing_user = User.objects(email=user.email).first()
if not existing_user:
    User.save(user)
else:
    print('User already exists')
# ==============================================

print('fetching all users...')
users = []
for user in User.objects():
    users.append(user.to_json())
print(users)

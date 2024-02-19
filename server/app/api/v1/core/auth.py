from models.users import User
from models.articles import Article
from models.platforms import Platform



# print('Creating User...')
# user = User(
#     username='admin',
#     email='admin@morya.com',
#     hashed_password='admin',
#     profile_picture='admin.png',
#     subscription_status='active',
#     authentication_provider='local',
#     is_active=True
# )
# existing_user = User.objects(email=user.email).first()
# if not existing_user:
#     User.save(user)
# else:
#     print('User already exists')

# print('Querying user')
# user = User.objects(email='admin@morya.com').first()
# print(user.to_json() if user else 'User not found')
# print('Done.')

# print('Updating User...')
# User.objects(email='admin@morya.com').update_one(
#     username='admina',
#     hashed_password='admin100'
# )

# print('Updated username and password')
# user = User.objects(email='admin@morya.com').first()
# print(user.to_json() if user else 'User not found')

# # ==============================================
# print('Creating User 2...')
# user = User(
#     username='Morya',
#     email='morayai@morya.com',
#     hashed_password='morya120',
#     profile_picture='morya.png',
#     subscription_status='active',
#     authentication_provider='google',
#     is_active=True
# )
# existing_user = User.objects(email=user.email).first()
# if not existing_user:
#     User.save(user)
# else:
#     print('User already exists')
# # ==============================================
# # ==============================================
# print('Creating User 3...')
# user = User(
#     username='Jason',
#     email='Jason@morya.com',
#     hashed_password='jason',
#     profile_picture='jason.png',
#     subscription_status='active',
#     authentication_provider='linkedin',
#     is_active=True
# )
# existing_user = User.objects(email=user.email).first()
# if not existing_user:
#     User.save(user)
# else:
#     print('User already exists')
# # ==============================================

# print('fetching all users...')
# users = [user.to_json() for user in User.objects()]
# print(users)

# print(f'Pre-deletion count: {User.objects.count()}')

# print('Deleting user...')
# email='admin@morya.com'
# existing_user = User.objects(email=email).first()
# if existing_user:
#     existing_user.delete()
# else:
#     print('You might have changed your email')

# print(f'Post-deletion count: {User.objects.count()}')

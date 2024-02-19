"""
Platform model for the containing all platofrm we support
- currently we support linkedin, medium and hashnode
- We will add more platforms as we go along
"""
import mongoengine as db

class Platform(db.Document):
    name = db.StringField(required=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    meta = {
        'collection': 'platforms'
    }

# Create and save a Platform document for LinkedIn
linkedin = Platform(
    name='LinkedIn',
    username='linkedin_api_key',  # Replace with your actual LinkedIn API key
    password='linkedin_api_secret'  # Replace with your actual LinkedIn API secret
)
linkedin.save()

# Create and save a Platform document for Medium
medium = Platform(
    name='Medium',
    username='medium_api_key',  # Replace with your actual Medium API key
    password='medium_api_secret'  # Replace with your actual Medium API secret
)
medium.save()

# Create and save a Platform document for Hashnode
hashnode = Platform(
    name='Hashnode',
    username='hashnode_api_key',  # Replace with your actual Hashnode API key
    password='hashnode_api_secret'  # Replace with your actual Hashnode API secret
)
hashnode.save()

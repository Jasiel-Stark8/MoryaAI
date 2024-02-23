# Initializes the Flask app and integrates app-wide configurations.
from flask import Flask
from .database import initialize_db

def create_app():
    app = Flask(__name__)
    app.config["DB_NAME"] = 'morya'
    app.config['DB_HOST'] = 'mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/'

    initialize_db(app)

    from models import platforms
    platforms.linkedin.save()
    platforms.medium.save()
    platforms.hashnode.save()

    return app

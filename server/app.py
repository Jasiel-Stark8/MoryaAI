"""Application entry point"""
import os
from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r'/api/v1/*': {'origins': '*'}})

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['BACKUP_SECRET_KEY'] = os.getenv('BACKUP_SECRET_KEY')

# import models
from app.models import users
from app.models import articles
from app.models import platforms
from app.models import published_content

# import blueprints
from app.api.v1.core.auth import auth
# from app.api.v1.core.generate import generate
# from app.api.v1.core.settings import settings
# from app.api.v1.core.subscribe import subscribe
# from app.api.v1.core.view_articles import view_articles

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
# app.register_blueprint(generate, url_prefix='/generate')
# app.register_blueprint(settings, url_prefix='/settings')
# app.register_blueprint(subscribe, url_prefix='/subscribe')
# app.register_blueprint(view_articles, url_prefix='/view_articles')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def landing_page(path):
    """
    This function serves as the landing page for the web application.

    Parameters:
        path (str): The path of the requested URL.

    Returns:
        str: The content of the 'index.html' file.

    """
    return app.send_static_file('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    """
    This function creates a new user account.

    Returns:
        str: A message indicating that the user account has been created.

    """
    data = request.get_json()
    user = User(
        username=data['username'],
        email=data['email'],
        hashed_password=data['hashed_password']
    )
    user.save()
    return jsonify({'message': 'User account created successfully!'})

@app.route('/login', methods=['POST'])
def login():
    """
    This function logs in a user.

    Returns:
        str: A message indicating that the user has been logged in.

    """
    data = request.get_json()
    user = User.objects(email=data['email']).first()
    if user and user.hashed_password == data['hashed_password']:
        return jsonify({'message': 'User logged in successfully!'})
    return jsonify({'message': 'Invalid email or password!'})


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)

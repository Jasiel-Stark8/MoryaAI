"""Application entry point"""
from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
from app.database import db
from app.api.v1.models import users
from app.api.v1.models.articles import Article
from app.api.v1.models.platforms import Platform
from app.api.v1.models.published_content import Published

app = Flask(__name__)
db.init_app(app)

CORS = CORS(app, resources={r'/api/*': {'origins': '*'}})

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

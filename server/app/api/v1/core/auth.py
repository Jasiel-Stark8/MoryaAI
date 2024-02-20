"""User Auth module"""
import logging
from flask import Flask, jsonify, request, session, Blueprint
from typing import Optional
import bcrypt
import secrets
from datetime import timedelta
from ratelimit import limits, sleep_and_retry
from mongoengine import errors
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models.users import User
from models.articles import Article
from models.platforms import Platform

# BLUEPRINT
auth = Blueprint('auth', __name__, url_prefix='/auth')

# Signup
logger = logging.getLogger(__name__)

@sleep_and_retry
@limits(calls=5, period=timedelta(seconds=60).total_seconds())
@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup(username: str, email: str, password: str):
    """
    Create a new user account.

    Args:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        dict: A JSON response containing the result of the signup operation.

    Raises:
        None
    """   

    def generate_verification_token():
        """
        Generate a random verification token.

        Returns:
            str: The generated verification token.
        """
        token = secrets.token_urlsafe(32)
        return token

    try:
        # Generate email verification token
        verification_token = generate_verification_token()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            profile_picture='',
            subscription_status='inactive',  # Set subscription status to inactive until user pays
            authentication_provider='local',
            is_active=False,  # Set user as inactive until email is verified
            verification_token=verification_token  # Store verification token in user object
        )
        existing_user = User.objects(email=user.email).first()
        if not existing_user:
            with session.start_transaction():
                User.save(user)
                logger.info('User created successfully')
                session['user_id'] = str(user.user_id)  # Store user ID in session

                # Send verification email to user
                send_verification_email(user.email, verification_token)

                return jsonify({'User created successfully'}, 201)
        else:
            logger.warning('User already exists')
            return jsonify({'User already exists'}, 400)
    except errors.NotUniqueError:
        logger.warning('User already exists')
        return jsonify({'User already exists'}, 400)
    except Exception as e:
        logger.error(f"An error occurred during signup: {str(e)}")
        return jsonify({'Error occurred during signup'}, 500)

def send_verification_email(email, verification_token):
    # Email configuration
    sender_email = 'MoryaAI.team@gmail.com'
    subject = 'Morya AI Email Verification'
    body = f'Please click the following link to verify your email: {verification_token}'

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject

    # Add body to the email
    message.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    # Create a secure connection with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    print('Verification email sent successfully')

# Verify Email
def verify_email():
    """
    Verify the email using the provided token.

    Returns:
        str: The verification result.
    """
    token = request.args.get('token')
    user = get_user_by_token(token)
    if user is not None:
        update_user(user, is_active=True)
        return 'Email verified successfully'
    return 'Invalid verification token', 400

def get_user_by_token(token: str) -> Optional[User]:
    """
    Get the user by the verification token.

    Args:
        token (str): The verification token.

    Returns:
        Optional[User]: The user object if found, None otherwise.
    """
    return User.objects(verification_token=token).first()

def update_user(user: User, is_active: bool):
    """
    Update the user's active status.

    Args:
        user (User): The user object.
        is_active (bool): The active status.
    """
    user.is_active = is_active
    user.save()


# Before Request
@auth.before_request
def check_user_verification():
    """
    Check if the user is verified before processing the request.
    """
    if request.endpoint != 'auth.verify_email':
        token = request.args.get('token')
        user = get_user_by_token(token)
        if user is None or not user.is_active:
            return jsonify({'error': 'User not verified'}, 401)


# Login
@sleep_and_retry
@limits(calls=5, period=timedelta(seconds=60).total_seconds())
@auth.route('/login', methods=['POST'], strict_slashes=False)
def login(email: str, password: str):
    user = User.objects(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return jsonify({'message': 'Login successful'}, 201)
        else:
            return jsonify({'error': 'Invalid password'}, 400)
    else:
        return jsonify({'error': 'User not found'}, 400)


# Verify Email
@auth.route('/verify_email', methods=['GET'], strict_slashes=False)
def verify_email():
    """
    Verify the email using the provided token.

    Returns:
        str: The verification result.
    """
    token = request.args.get('token')
    user = get_user_by_token(token)
    if user is not None:
        update_user(user, is_active=True)
        return jsonify({'message': 'Email verified successfully'})
    return jsonify({'error': 'Invalid verification token'}, 400)

# Logout
@auth.route('/logout', methods=['GET'], strict_slashes=False)
def logout(user_id: str):
    """
    Logout the user.

    Returns:
        str: The logout result.
    """
    session.pop(user_id, None)
    return jsonify({'message': 'Logout successful'})


# Google Authentication
def google_auth(user_info: dict):
    # Store user_info to the database
    # Example code:
    user = User(
        username=user_info['username'],
        email=user_info['email'],
        hashed_password='',
        profile_picture=user_info['profile_picture'],
        subscription_status='active',
        authentication_provider='google',
        is_active=True
    )
    existing_user = User.objects(email=user.email).first()
    if not existing_user:
        User.save(user)
        return 'User created successfully'
    else:
        return 'User already exists'

# LinkedIn Authentication
def linkedin_auth(user_info):
    # Store user_info to the database
    # Example code:
    user = User(
        username=user_info['username'],
        email=user_info['email'],
        hashed_password='',
        profile_picture=user_info['profile_picture'],
        subscription_status='active',
        authentication_provider='linkedin',
        is_active=True
    )
    existing_user = User.objects(email=user.email).first()
    if not existing_user:
        User.save(user)
        return 'User created successfully'
    else:
        return 'User already exists'

"""User Auth module"""
import logging
from flask import Flask, jsonify, request, session, Blueprint, render_template
from typing import Optional
import bcrypt
import secrets
from datetime import timedelta
from ratelimit import limits, sleep_and_retry
from mongoengine import errors
from app.models.users import User
from app.models.articles import Article
from app.models.platforms import Platform
from flask_mail import Mail, Message

# BLUEPRINT
auth = Blueprint('auth', __name__, url_prefix='/auth')
logger = logging.getLogger(__name__)
mail = Mail()


# Before Request
@auth.before_request
def check_user_verification():
    """
    Check if the user is verified and registered before processing the request.
    """
    if not session.get('user_id'):
        return jsonify({'error': 'Unauthorized access'}), 401

    user = User.objects(id=session['user_id']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not user.is_active:
        return jsonify({'error': 'Your account is not verified. \
                        Please check your email for verification instructions.'}), 401


# Signup
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
    # Generate verification token
    def generate_verification_token(user: User) -> str:
        """
        Generate a verification token for the user.

        Args:
            user (User): The user object.

        Returns:
            str: The verification token.
        """
        # Generate a unique verification token
        token = secrets.token_urlsafe(32)
        # Save the token to the user object
        user.verification_token = token
        user.save()
        return token

    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            profile_picture='',
            subscription_status='inactive',  # Set subscription status to inactive until user pays us lol
            authentication_provider='local',
            is_active=False,  # Set user as inactive until email is verified
            verification_token=verification_token  # Store verification token in user object
        )

        # Call generate_verification_token function to generate a verification token
        verification_token=generate_verification_token(user)

        existing_user = User.objects(email=user.email).first()
        if not existing_user:
            with session.start_transaction():
                User.save(user)
                logger.info('User created successfully')
                session['user_id'] = str(user.user_id)  # Store user ID in session

                # Send verification email
                msg = Message('Email Verification', recipients=[email])
                msg.body = f"Please click the following link to verify your email: \
                        {request.host_url}auth/verify_email?token={verification_token}"
                mail.send(msg)

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

# Once verified activate user status
def update_user(user: User):
    """
    Update the user's active status.

    Args:
        user (User): The user object.
        is_active (bool): The active status.
    """
    user.is_active = True
    user.save()

# Login
@sleep_and_retry
@limits(calls=5, period=timedelta(seconds=60).total_seconds())
@auth.route('/login', methods=['POST'], strict_slashes=False)
def login(email: str, password: str):
    user = User.objects(email=email).first()
    if user:
        if user.is_active:  # Check if user is verified
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
                return jsonify({'message': 'Login successful'}, 201)
            else:
                return jsonify({'error': 'Invalid credentials'}, 400)
        else:
            return jsonify({'error': 'Your account is not verified. \
                            Please check your email for verification instructions.'}, 401)
    else:
        return jsonify({'error': 'You don\'t seem to have an account. \
                        Please sign up to create an account.'}, 400)

# Verify Email
@auth.route('/verify_email', methods=['GET'], strict_slashes=False)
def verify_email():
    """
    Verify the email using the provided token.

    Returns:
        str: The verification result.
    """
    token = request.args.get('token')
    user = User.objects(token=token).first()
    if user is not None:
        update_user(user)
        return jsonify({'Email verified successfully'}, 200)
    else:
        return jsonify({'Invalid token'}, 400)

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

# Reset Password
@auth.route('/reset_password', methods=['POST'])
def reset_password():
    """Reset Password"""
    email = request.form.get('email')
    new_password = request.form.get('new_password')
    user = User.objects(email=email).first()
    if user is not None:
        user.password = new_password
        user.save()
        return 'Password reset successful'
    else:
        return 'User not found'


# # Google Authentication
# def google_auth(user_info: dict):
#     # Store user_info to the database
#     # Example code:
#     user = User(
#         username=user_info['username'],
#         email=user_info['email'],
#         hashed_password='',
#         profile_picture=user_info['profile_picture'],
#         subscription_status='active',
#         authentication_provider='google',
#         is_active=True
#     )
#     existing_user = User.objects(email=user.email).first()
#     if not existing_user:
#         User.save(user)
#         return 'User created successfully'
#     else:
#         return 'User already exists'

# # LinkedIn Authentication
# def linkedin_auth(user_info):
#     # Store user_info to the database
#     # Example code:
#     user = User(
#         username=user_info['username'],
#         email=user_info['email'],
#         hashed_password='',
#         profile_picture=user_info['profile_picture'],
#         subscription_status='active',
#         authentication_provider='linkedin',
#         is_active=True
#     )
#     existing_user = User.objects(email=user.email).first()
#     if not existing_user:
#         User.save(user)
#         return 'User created successfully'
#     else:
#         return 'User already exists'

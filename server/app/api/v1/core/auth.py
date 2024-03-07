"""User Auth module"""
import logging
from flask import Flask, jsonify, request, session, Blueprint, render_template
from typing import Optional
import bcrypt
import secrets
import json
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
    Check if the user is verified and registered before processing the request,
    except for unrestricted routes like signup.
    """
    unrestricted_routes = ['auth.signup']
    if request.endpoint in unrestricted_routes:
        return  # Skip the checks below for unrestricted routes

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
def signup():
    """
    Create a new user account.
    """
    if not request.is_json:
        return jsonify({'error': 'Missing JSON in request'}), 400

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate the presence of all required fields
    if not all([username, email, password]):
        return jsonify({'error': 'Missing data for username, email, or password'}), 400

    try:
        # Check if user already exists
        existing_user = User.objects(email=email).first()
        if existing_user:
            return jsonify({'error': 'User already exists'}), 400
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            is_active=False  # Set user as inactive until email is verified
        ).save()  # Save the user and then generate the verification token

        # Generate and save verification token
        verification_token = secrets.token_urlsafe(32)
        user.update(set__verification_token=verification_token)

        # Send verification email
        msg = Message('Email Verification', recipients=[email])
        msg.body = f"Please click the following link to verify your email: \
                    {request.host_url}auth/verify_email?token={verification_token}"
        mail.send(msg)

        return jsonify({'message': 'User created successfully. Please check your email to verify your account.'}), 201
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

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

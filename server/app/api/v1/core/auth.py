"""User Auth module"""
import logging
from flask import Flask, jsonify, request, session, Blueprint, render_template
from typing import Optional
import bcrypt
from datetime import timedelta
from ratelimit import limits, sleep_and_retry
from mongoengine import errors
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

implement verification email with flask-mail simply
# Once verified activate user status
def update_user(user: User, is_active: bool):
    """
    Update the user's active status.

    Args:
        user (User): The user object.
        is_active (bool): The active status.
    """
    user.is_active = True
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

# Reset Password
@auth.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    email = request.form.get('email')
    user = get_user_by_email(email)
    if user is not None:
        token = generate_reset_token(user)
        send_password_reset_email(user.email, token)
    return 'Password reset email sent'

@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        token = request.form.get('token')
        new_password = request.form.get('new_password')
        user = validate_reset_token(token)
        if user is not None:
            update_password(user, new_password)
            return 'Password reset successfully'
        else:
            return 'Invalid or expired reset token', 400
    else:
        return render_template('reset_password.html')

def send_password_reset_email(email, token):
    sender_email = "your_email@example.com"
    receiver_email = email
    password = "your_password"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Password Reset"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""\
    Hi,
    You have requested to reset your password. Please click the link below to reset your password:
    http://your_website.com/reset-password?token={token}"""

    html = f"""\
    <html>
      <body>
        <p>Hi,<br>
           You have requested to reset your password. Please click the link below to reset your password:<br>
           <a href="http://your_website.com/reset-password?token={token}">Reset Password</a>
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())



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

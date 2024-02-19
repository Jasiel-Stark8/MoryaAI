"""User Auth module"""
from flask import Flask, jsonify, request
import logging
from models.users import User
from models.articles import Article
from models.platforms import Platform
import bcrypt

# Signup
def signup(username, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        profile_picture='',
        subscription_status='active',
        authentication_provider='local',
        is_active=True
    )
    existing_user = User.objects(email=user.email).first()
    if not existing_user:
        User.save(user)
        return jsonify({'User created successfully'}, 201)
    else:
        return jsonify({'User already exists'}, 400)

# Login
def login(email, password):
    user = User.objects(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return jsonify({'Login successful'}, 201)
        else:
            return jsonify({'Invalid password'}, 400)
    else:
        return jsonify({'User not found'}, 400)

# Google Authentication
def google_auth(user_info):
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

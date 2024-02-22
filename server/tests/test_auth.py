import unittest
import os
import sys
from flask import session, jsonify, request
from app.api.v1.core.auth import signup, verify_email, update_user, login, logout, reset_password
from app.api.v1.models.users import User

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_signup(self):
        with self.app.test_request_context():
            response = signup('testuser', 'test@example.com', 'test_password')
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'message': 'User created successfully'})

    def test_verify_email(self):
        with self.app.test_request_context():
            # Create a user and get the verification token
            signup('testuser', 'test@example.com', 'test_password')
            user = User.objects(email='test@example.com').first()
            token = user.verification_token

            # Verify the email using the token
            response = verify_email(token)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Email verified successfully'})

    def test_login(self):
        with self.app.test_request_context():
            # Create a user
            signup('testuser', 'test@example.com', 'test_password')

            # Login with correct credentials
            response = login('test@example.com', 'test_password')
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'message': 'Login successful'})

            # Login with incorrect password
            response = login('test@example.com', 'wrong_password')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

            # Login with unverified email
            user = User.objects(email='test@example.com').first()
            user.is_active = False
            user.save()
            response = login('test@example.com', 'test_password')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Your account is not verified.\
                            Please check your email for verification instructions.'})

            # Login with non-existent email
            response = login('nonexistent@example.com', 'test_password')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'You don\'t seem to have an account. \
                            Please sign up to create an account.'})

    def test_logout(self):
        with self.app.test_request_context():
            # Create a user and login
            signup('testuser', 'test@example.com', 'test_password')
            login('test@example.com', 'test_password')

            # Logout
            response = logout()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Logout successful'})

    def test_reset_password(self):
        with self.app.test_request_context():
            # Create a user
            signup('testuser', 'test@example.com', 'test_password')

            # Reset password
            response = reset_password('test@example.com', 'new_password')
            self.assertEqual(response, 'Password reset successful')

            # Login with new password
            response = login('test@example.com', 'new_password')
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'message': 'Login successful'})

if __name__ == '__main__':
    unittest.main()

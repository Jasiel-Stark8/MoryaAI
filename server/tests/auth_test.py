import unittest
from app.api.v1.core.auth import signup, login

class TestAuth(unittest.TestCase):
    def test_register(self):
        # Test for successful registration
        assert response = signup('testuser',
                            'test@email.com',
                            'test_password')
        
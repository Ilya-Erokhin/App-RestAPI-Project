from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):

    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', json={'username': 'Ilia', 'password': 'lfHd41Jau'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('Ilia'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(response.data)) # json.loads() - Converted to a Dict, in order to Compare 2 Dictionaries

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', json={'username': 'Ilia', 'password': 'lfHd41Jau'})
            # Login - using "/auth" endpoint
                auth_response = client.post('/auth',
                                           json={'username': 'Ilia', 'password': 'lfHd41Jau'},
                                           headers={'Content-Type': 'application/json'})

    # Converting the Data from Response (auth_response), takes KEYS from dict (username, password),
        # this keys() will return in a LIST like - ['access_token'] and COMPARE IT with "assertIn"
                self.assertIn('access_token', json.loads(auth_response.data).keys())


    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', json={'username': 'Ilia', 'password': 'lfHd41Jau'})
                response = client.post('/register', json={'username': 'Ilia', 'password': 'lfHd41Jau'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'A user with that username already exists.'},
                                     json.loads(response.data))
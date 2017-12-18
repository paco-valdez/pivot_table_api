#!/usr/bin/python
import unittest
import json
import base64
from mock import patch
import api


class UserTests(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_user_creation(self):
        with patch('models.db.session'):
            response = self.app.post('/user',
                                     data={'username': 'demo', 'password': 'demo'},
                                     headers={'Authorization': 'Basic '+base64.b64encode('demo:demo')})
            print response.data
            data = json.loads(response.data.decode())
            self.assertTrue(isinstance(data, dict))
            self.assertIn('status', data)
            self.assertEquals(data['status'], 'success')

    def test_get_user(self):
        with patch('models.user.User'):
            response = self.app.get('/user/123131',
                                    headers={'Authorization': 'Basic '+base64.b64encode('demo:demo')})
            print response.data
            data = json.loads(response.data.decode())
            self.assertTrue(isinstance(data, dict))
            self.assertIn('status', data)
            self.assertEquals(data['status'], 'error')


if __name__ == '__main__':
    unittest.main()

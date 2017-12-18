#!/usr/bin/python
import unittest
import json
import base64
from mock import patch
import api


class DataResourceTests(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_isochrone_parameters(self):
        with patch('models.db.session.query'):
            response = self.app.get('/dataset/test_dataset',
                                    headers={'Authorization': 'Basic '+base64.b64encode('demo:demo')})
            data = json.loads(response.data.decode())
            self.assertIn('status', data)


class SpecTests(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_isochrone_parameters(self):
        response = self.app.get('/spec',
                                headers={'Authorization': 'Basic '+base64.b64encode('demo:demo')})
        data = json.loads(response.data.decode())
        self.assertIn('columns', data)


if __name__ == '__main__':
    unittest.main()

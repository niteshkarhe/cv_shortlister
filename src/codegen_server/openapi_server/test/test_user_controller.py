import unittest

from flask import json

from openapi_server.models.user_object import UserObject  # noqa: E501
from openapi_server.models.user_request import UserRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_user_response(self):
        """Test case for get_user_response

        To store user data for given question
        """
        user_request = {"email":"email","name":"name","role":"role","question":"question","answer":"answer"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'accept_version': 'v1',
        }
        response = self.client.open(
            '/api/user',
            method='POST',
            headers=headers,
            data=json.dumps(user_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

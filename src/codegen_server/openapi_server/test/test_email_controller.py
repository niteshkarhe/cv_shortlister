import unittest

from flask import json

from openapi_server.models.email_request import EmailRequest  # noqa: E501
from openapi_server.models.send_email_object import SendEmailObject  # noqa: E501
from openapi_server.test import BaseTestCase


class TestEmailController(BaseTestCase):
    """EmailController integration test stubs"""

    def test_send_email(self):
        """Test case for send_email

        To send email to shortlisted candidates
        """
        email_request = {"name":"name","email":"email","login_code":"login_code"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'accept_version': 'v1',
        }
        response = self.client.open(
            '/api/email',
            method='POST',
            headers=headers,
            data=json.dumps(email_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

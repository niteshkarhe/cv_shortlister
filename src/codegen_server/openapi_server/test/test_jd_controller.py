import unittest

from flask import json

from openapi_server.models.status import Status  # noqa: E501
from openapi_server.test import BaseTestCase


class TestJdController(BaseTestCase):
    """JdController integration test stubs"""

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_upload_jd(self):
        """Test case for upload_jd

        To upload JD
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'accept_version': 'v1',
        }
        data = dict(file='/path/to/file')
        response = self.client.open(
            '/api/jd/upload',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

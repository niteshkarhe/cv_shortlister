import unittest

from flask import json

from openapi_server.models.status import Status  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSwaggerUiController(BaseTestCase):
    """SwaggerUiController integration test stubs"""

    def test_load_swagger_ui(self):
        """Test case for load_swagger_ui

        load swagger ui
        """
        headers = { 
            'Accept': 'application/json',
            'accept_version': 'v1',
            'Authorization': 'Basic Zm9vOmJhcg==',
        }
        response = self.client.open(
            '/api/docs/swagger_ui',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

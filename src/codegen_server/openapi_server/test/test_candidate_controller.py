import unittest

from flask import json

from openapi_server.models.get_candidate_object import GetCandidateObject  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCandidateController(BaseTestCase):
    """CandidateController integration test stubs"""

    def test_get_candidate_questions(self):
        """Test case for get_candidate_questions

        To get the candidate and question details
        """
        query_string = [('email', 'email_example'),
                        ('login_code', 'login_code_example')]
        headers = { 
            'Accept': 'application/json',
            'accept_version': 'v1',
        }
        response = self.client.open(
            '/api/candidates',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

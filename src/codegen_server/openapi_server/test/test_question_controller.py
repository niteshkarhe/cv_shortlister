import unittest

from flask import json

from openapi_server.models.question_object import QuestionObject  # noqa: E501
from openapi_server.test import BaseTestCase


class TestQuestionController(BaseTestCase):
    """QuestionController integration test stubs"""

    def test_get_questions(self):
        """Test case for get_questions

        To get the question details
        """
        query_string = [('job_id', 'job_id_example')]
        headers = { 
            'Accept': 'application/json',
            'accept_version': 'v1',
        }
        response = self.client.open(
            '/api/question',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

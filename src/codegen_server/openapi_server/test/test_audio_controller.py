import unittest

from flask import json

from openapi_server.models.audio_object import AudioObject  # noqa: E501
from openapi_server.models.audio_request import AudioRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAudioController(BaseTestCase):
    """AudioController integration test stubs"""

    def test_get_audio(self):
        """Test case for get_audio

        To capture the audio and convert it to text and store the result
        """
        audio_request = {"question":"question","start_recording":"start_recording"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'accept_version': 'v1',
        }
        response = self.client.open(
            '/api/audio',
            method='POST',
            headers=headers,
            data=json.dumps(audio_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

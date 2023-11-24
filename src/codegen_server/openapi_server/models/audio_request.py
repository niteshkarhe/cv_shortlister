from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class AudioRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, question=None, start_recording=None):  # noqa: E501
        """AudioRequest - a model defined in OpenAPI

        :param question: The question of this AudioRequest.  # noqa: E501
        :type question: str
        :param start_recording: The start_recording of this AudioRequest.  # noqa: E501
        :type start_recording: bool
        """
        self.openapi_types = {
            'question': str,
            'start_recording': bool
        }

        self.attribute_map = {
            'question': 'question',
            'start_recording': 'start_recording'
        }

        self._question = question
        self._start_recording = start_recording

    @classmethod
    def from_dict(cls, dikt) -> 'AudioRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AudioRequest of this AudioRequest.  # noqa: E501
        :rtype: AudioRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def question(self) -> str:
        """Gets the question of this AudioRequest.


        :return: The question of this AudioRequest.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question: str):
        """Sets the question of this AudioRequest.


        :param question: The question of this AudioRequest.
        :type question: str
        """
        if question is None:
            raise ValueError("Invalid value for `question`, must not be `None`")  # noqa: E501

        self._question = question

    @property
    def start_recording(self) -> bool:
        """Gets the start_recording of this AudioRequest.


        :return: The start_recording of this AudioRequest.
        :rtype: bool
        """
        return self._start_recording

    @start_recording.setter
    def start_recording(self, start_recording: bool):
        """Sets the start_recording of this AudioRequest.


        :param start_recording: The start_recording of this AudioRequest.
        :type start_recording: bool
        """
        if start_recording is None:
            raise ValueError("Invalid value for `start_recording`, must not be `None`")  # noqa: E501

        self._start_recording = start_recording
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class SaveQuestionObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None):  # noqa: E501
        """SaveQuestionObject - a model defined in OpenAPI

        :param message: The message of this SaveQuestionObject.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SaveQuestionObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SaveQuestionObject of this SaveQuestionObject.  # noqa: E501
        :rtype: SaveQuestionObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this SaveQuestionObject.


        :return: The message of this SaveQuestionObject.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SaveQuestionObject.


        :param message: The message of this SaveQuestionObject.
        :type message: str
        """

        self._message = message

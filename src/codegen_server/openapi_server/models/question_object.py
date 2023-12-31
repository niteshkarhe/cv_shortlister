from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class QuestionObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, questions=None, role=None):  # noqa: E501
        """QuestionObject - a model defined in OpenAPI

        :param questions: The questions of this QuestionObject.  # noqa: E501
        :type questions: List[str]
        :param role: The role of this QuestionObject.  # noqa: E501
        :type role: str
        """
        self.openapi_types = {
            'questions': List[str],
            'role': str
        }

        self.attribute_map = {
            'questions': 'questions',
            'role': 'role'
        }

        self._questions = questions
        self._role = role

    @classmethod
    def from_dict(cls, dikt) -> 'QuestionObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QuestionObject of this QuestionObject.  # noqa: E501
        :rtype: QuestionObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def questions(self) -> List[str]:
        """Gets the questions of this QuestionObject.


        :return: The questions of this QuestionObject.
        :rtype: List[str]
        """
        return self._questions

    @questions.setter
    def questions(self, questions: List[str]):
        """Sets the questions of this QuestionObject.


        :param questions: The questions of this QuestionObject.
        :type questions: List[str]
        """

        self._questions = questions

    @property
    def role(self) -> str:
        """Gets the role of this QuestionObject.


        :return: The role of this QuestionObject.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this QuestionObject.


        :param role: The role of this QuestionObject.
        :type role: str
        """

        self._role = role

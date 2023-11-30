from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class QuestionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, role=None, hr_email=None, question=None, expected_answer=None):  # noqa: E501
        """QuestionRequest - a model defined in OpenAPI

        :param id: The id of this QuestionRequest.  # noqa: E501
        :type id: int
        :param role: The role of this QuestionRequest.  # noqa: E501
        :type role: str
        :param hr_email: The hr_email of this QuestionRequest.  # noqa: E501
        :type hr_email: str
        :param question: The question of this QuestionRequest.  # noqa: E501
        :type question: str
        :param expected_answer: The expected_answer of this QuestionRequest.  # noqa: E501
        :type expected_answer: str
        """
        self.openapi_types = {
            'id': int,
            'role': str,
            'hr_email': str,
            'question': str,
            'expected_answer': str
        }

        self.attribute_map = {
            'id': 'id',
            'role': 'role',
            'hr_email': 'hr_email',
            'question': 'question',
            'expected_answer': 'expected_answer'
        }

        self._id = id
        self._role = role
        self._hr_email = hr_email
        self._question = question
        self._expected_answer = expected_answer

    @classmethod
    def from_dict(cls, dikt) -> 'QuestionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QuestionRequest of this QuestionRequest.  # noqa: E501
        :rtype: QuestionRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this QuestionRequest.


        :return: The id of this QuestionRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this QuestionRequest.


        :param id: The id of this QuestionRequest.
        :type id: int
        """

        self._id = id

    @property
    def role(self) -> str:
        """Gets the role of this QuestionRequest.


        :return: The role of this QuestionRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this QuestionRequest.


        :param role: The role of this QuestionRequest.
        :type role: str
        """

        self._role = role

    @property
    def hr_email(self) -> str:
        """Gets the hr_email of this QuestionRequest.


        :return: The hr_email of this QuestionRequest.
        :rtype: str
        """
        return self._hr_email

    @hr_email.setter
    def hr_email(self, hr_email: str):
        """Sets the hr_email of this QuestionRequest.


        :param hr_email: The hr_email of this QuestionRequest.
        :type hr_email: str
        """

        self._hr_email = hr_email

    @property
    def question(self) -> str:
        """Gets the question of this QuestionRequest.


        :return: The question of this QuestionRequest.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question: str):
        """Sets the question of this QuestionRequest.


        :param question: The question of this QuestionRequest.
        :type question: str
        """

        self._question = question

    @property
    def expected_answer(self) -> str:
        """Gets the expected_answer of this QuestionRequest.


        :return: The expected_answer of this QuestionRequest.
        :rtype: str
        """
        return self._expected_answer

    @expected_answer.setter
    def expected_answer(self, expected_answer: str):
        """Sets the expected_answer of this QuestionRequest.


        :param expected_answer: The expected_answer of this QuestionRequest.
        :type expected_answer: str
        """

        self._expected_answer = expected_answer

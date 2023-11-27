from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class UserRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, name=None, role=None, question=None):  # noqa: E501
        """UserRequest - a model defined in OpenAPI

        :param email: The email of this UserRequest.  # noqa: E501
        :type email: str
        :param name: The name of this UserRequest.  # noqa: E501
        :type name: str
        :param role: The role of this UserRequest.  # noqa: E501
        :type role: str
        :param question: The question of this UserRequest.  # noqa: E501
        :type question: str
        """
        self.openapi_types = {
            'email': str,
            'name': str,
            'role': str,
            'question': str
        }

        self.attribute_map = {
            'email': 'email',
            'name': 'name',
            'role': 'role',
            'question': 'question'
        }

        self._email = email
        self._name = name
        self._role = role
        self._question = question

    @classmethod
    def from_dict(cls, dikt) -> 'UserRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserRequest of this UserRequest.  # noqa: E501
        :rtype: UserRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this UserRequest.


        :return: The email of this UserRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserRequest.


        :param email: The email of this UserRequest.
        :type email: str
        """

        self._email = email

    @property
    def name(self) -> str:
        """Gets the name of this UserRequest.


        :return: The name of this UserRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserRequest.


        :param name: The name of this UserRequest.
        :type name: str
        """

        self._name = name

    @property
    def role(self) -> str:
        """Gets the role of this UserRequest.


        :return: The role of this UserRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this UserRequest.


        :param role: The role of this UserRequest.
        :type role: str
        """

        self._role = role

    @property
    def question(self) -> str:
        """Gets the question of this UserRequest.


        :return: The question of this UserRequest.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question: str):
        """Sets the question of this UserRequest.


        :param question: The question of this UserRequest.
        :type question: str
        """

        self._question = question

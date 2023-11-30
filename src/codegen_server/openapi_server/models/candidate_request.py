from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class CandidateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, email=None, jobid=None):  # noqa: E501
        """CandidateRequest - a model defined in OpenAPI

        :param name: The name of this CandidateRequest.  # noqa: E501
        :type name: str
        :param email: The email of this CandidateRequest.  # noqa: E501
        :type email: str
        :param jobid: The jobid of this CandidateRequest.  # noqa: E501
        :type jobid: int
        """
        self.openapi_types = {
            'name': str,
            'email': str,
            'jobid': int
        }

        self.attribute_map = {
            'name': 'name',
            'email': 'email',
            'jobid': 'jobid'
        }

        self._name = name
        self._email = email
        self._jobid = jobid

    @classmethod
    def from_dict(cls, dikt) -> 'CandidateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CandidateRequest of this CandidateRequest.  # noqa: E501
        :rtype: CandidateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CandidateRequest.


        :return: The name of this CandidateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CandidateRequest.


        :param name: The name of this CandidateRequest.
        :type name: str
        """

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this CandidateRequest.


        :return: The email of this CandidateRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this CandidateRequest.


        :param email: The email of this CandidateRequest.
        :type email: str
        """

        self._email = email

    @property
    def jobid(self) -> int:
        """Gets the jobid of this CandidateRequest.


        :return: The jobid of this CandidateRequest.
        :rtype: int
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid: int):
        """Sets the jobid of this CandidateRequest.


        :param jobid: The jobid of this CandidateRequest.
        :type jobid: int
        """

        self._jobid = jobid
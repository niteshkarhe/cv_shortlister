import connexion
import six

from openapi_server.models.email_request import EmailRequest  # noqa: E501
from openapi_server.models.send_email_object import SendEmailObject  # noqa: E501
from openapi_server.server_impl.email_controller_impl import Email_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def send_email(accept_version=None, email_request=None):  # noqa: E501
    """To send email to shortlisted candidates

    This API is used to send email to shortlisted candidates # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param email_request: 
    :type email_request: dict | bytes

    :rtype: SendEmailObject
    """
    if connexion.request.is_json:
        email_request = EmailRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.send_email(accept_version, email_request)

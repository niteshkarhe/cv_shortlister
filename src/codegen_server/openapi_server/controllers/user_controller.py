import connexion
import six

from openapi_server.models.user_object import UserObject  # noqa: E501
from openapi_server.models.user_request import UserRequest  # noqa: E501
from openapi_server.server_impl.user_controller_impl import User_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def save_user_response(accept_version=None, user_request=None):  # noqa: E501
    """To store user data for given question

    This API is used to store user response in database # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param user_request: 
    :type user_request: dict | bytes

    :rtype: UserObject
    """
    if connexion.request.is_json:
        user_request = UserRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.save_user_response(accept_version, user_request)

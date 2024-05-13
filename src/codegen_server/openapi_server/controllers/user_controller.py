import connexion
import six

from openapi_server.models.get_user_data_object import GetUserDataObject  # noqa: E501
from openapi_server.models.user_object import UserObject  # noqa: E501
from openapi_server.models.user_request import UserRequest  # noqa: E501
from openapi_server.server_impl.user_controller_impl import User_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def delete_particular_user_data(user_id, accept_version=None):  # noqa: E501
    """To delete the user details

    This API is used to delete the user response of particular id # noqa: E501

    :param user_id: 
    :type user_id: str
    :param accept_version: 
    :type accept_version: str

    :rtype: str
    """

    impl = serviceImpl()

    return impl.delete_particular_user_data(user_id, accept_version)



def delete_userdata(accept_version=None):  # noqa: E501
    """To delete the user data

    This API is used to delete all user records # noqa: E501

    :param accept_version: 
    :type accept_version: str

    :rtype: str
    """

    impl = serviceImpl()

    return impl.delete_userdata(accept_version)



def get_userdata(accept_version=None):  # noqa: E501
    """To get the user data

    This API is used to get all user data # noqa: E501

    :param accept_version: 
    :type accept_version: str

    :rtype: GetUserDataObject
    """

    impl = serviceImpl()

    return impl.get_userdata(accept_version)



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

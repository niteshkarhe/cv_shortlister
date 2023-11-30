import connexion
import six

from openapi_server.models.respone_object import ResponeObject  # noqa: E501
from openapi_server.server_impl.jd_controller_impl import Jd_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def upload_jd(accept_version=None, file=None):  # noqa: E501
    """To upload JD

    This API is used to upload JD # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param file: 
    :type file: str

    :rtype: ResponeObject
    """

    impl = serviceImpl()

    return impl.upload_jd(accept_version, file)

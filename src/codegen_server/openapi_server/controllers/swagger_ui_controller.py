import connexion
import six

from openapi_server.models.status import Status  # noqa: E501
from openapi_server.server_impl.swagger_ui_controller_impl import Swagger_ui_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def load_swagger_ui(accept_version=None):  # noqa: E501
    """load swagger ui

     # noqa: E501

    :param accept_version: 
    :type accept_version: str

    :rtype: Status
    """

    impl = serviceImpl()

    return impl.load_swagger_ui(accept_version)

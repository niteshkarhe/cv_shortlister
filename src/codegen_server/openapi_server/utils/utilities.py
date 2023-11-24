import connexion
from openapi_server.app_context import get_logger

logger = get_logger()

class utils:
    @staticmethod
    def get_api_version(accept_version=None):
        if accept_version is None:
            version_info = connexion.request.headers.get(
                "accept_version", None
            )
        else:
            version_info = accept_version
        return version_info
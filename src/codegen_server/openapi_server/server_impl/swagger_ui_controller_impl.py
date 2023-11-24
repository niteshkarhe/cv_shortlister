from flask import send_file
import os
from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting


class Swagger_ui_controller_Impl:
    @wrap(log_entering, log_exiting)
    def load_swagger_ui(self, accept_version):
        file_path = os.path.join(os.path.abspath(os.curdir),
                                 "openapi_server", "openapi", "openapi.yaml")
        return send_file(file_path)
from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_users import Db_Users
from openapi_server.models.user_object import UserObject
from openapi_server.models.users_model import UsersModel

from datetime import datetime
from sqlalchemy import text

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class User_controller_Impl:
    __controller__ = "User"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def save_user_response(self, accept_version, user_request):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            date_format = "%Y-%m-%d %H:%M:%S"
            try:
                Db_Users().delete()
                db_users_obj = Db_Users(
                    email = user_request.email,
                    name = user_request.name,
                    role = user_request.role,
                    question = user_request.question,
                    answer = '',
                    percentage = 100,
                    result = 'Passed',
                    recordingpath = '',
                    date = datetime.strptime(datetime.utcnow().strftime(date_format), date_format)
                )

                db_users_obj.add()
                resp = []
                users = Db_Users.get_all()
                for user in users:
                    print(user.id)
                    print(user.email)
                    resp.append(
                        UsersModel(
                            id=user.id,
                            email=user.email,
                            name=user.name,
                            role=user.role,
                            question=user.question,
                            answer=user.answer,
                            percentage=user.percentage,
                            result=user.result,
                            recordingpath=user.recordingpath,
                            _date=user.date.strftime(date_format)
                        )
                    )

                print(resp)

                #return resp, 200
                return UserObject(id=db_users_obj.id), 200
                #return "", 200

            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)


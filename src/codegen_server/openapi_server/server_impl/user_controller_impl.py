from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_users import Db_Users
from openapi_server.models.user_object import UserObject
from openapi_server.models.get_user_data_object import GetUserDataObject
from openapi_server.models.users_model import UsersModel

from datetime import datetime
from sqlalchemy import text
from flask import jsonify, make_response

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
            add_date = datetime.strptime(datetime.utcnow().strftime(date_format), date_format)
            try:
                db_users_obj = Db_Users(
                    email = user_request.email,
                    name = user_request.name,
                    role = user_request.role,
                    question = user_request.question,
                    answer = user_request.answer,
                    percentage = 100,
                    result = 'Passed',
                    recordingpath = '',
                    date = add_date
                )

                db_users_obj.add()
                db.session.refresh(db_users_obj)
                return UserObject(id=db_users_obj.id), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def get_userdata(self, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                users = Db_Users.get_all()
                if users is None:
                    return Error(code=404, message="No user data present"), 404
                if users[0] is not None:
                    resp = []
                    for user in users:
                        resp.append(GetUserDataObject(
                            id=user.id,
                            name=user.name,
                            email=user.email,
                            role=user.role,
                            question=user.question,
                            answer=user.answer,
                            percentage=user.percentage,
                            result=user.result,
                            recordingpath=user.recordingpath,
                            _date=user.date
                        ))

                    return resp, 200
                else:
                    return Error(code=404, message="No user data present"), 404
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    def delete_userdata(self, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                Db_Users().delete()
                return make_response(jsonify({'message': 'User record deleted successfully'})), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    def delete_particular_user_data(self, user_id, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                db.session.execute(text(
                    "delete from users where id = " + str(user_id)
                ))
                db.session.commit()
                return make_response(jsonify({'message': 'User question details are deleted successfully'})), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)
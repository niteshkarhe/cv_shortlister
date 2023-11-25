from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.models.save_question_object import SaveQuestionObject

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Question_controller_Impl:
    __controller__ = "Question"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def save_questions(self, accept_version, question_request):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                db_question_obj = Db_Questions(
                    role=question_request.role,
                    hr_email=question_request.hr_email,
                    question=question_request.question,
                    expected_answer=question_request.expected_answer
                )

                db_question_obj.add()

                return SaveQuestionObject(message="Question details saved successfully"), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def get_all_questions(self, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                questions = Db_Questions.get_all()
                resp = []
                for question in questions:
                    dict = {}
                    dict["id"] = question.id
                    dict["role"] = question.role
                    dict["hr_email"] = question.hr_email
                    dict["question"] = question.question
                    dict["expected_answer"] = question.expected_answer
                    resp.append(dict)

                return resp, 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)
from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_jobs import Db_Jobs
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.models.save_job_object import SaveJobObject
from openapi_server.models.question_object import QuestionObject
from openapi_server.models.get_job_object import GetJobObject

from sqlalchemy import text

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Job_controller_Impl:
    __controller__ = "Job"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def get_jobs(self, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                jobs = Db_Jobs.get_jobs()
                resp = []
                if jobs is not None:
                    for job in jobs:
                        resp.append(
                            GetJobObject(
                                job_id=job.id,
                                role=job.role,
                                hr_email=job.hr_email
                            )
                        )

                    return resp, 200
                else:
                    return Error(code=404, message="No job records are present"), 404
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def get_jobid_questions(self, job_id, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                job = Db_Jobs.get_jobid_deails(job_id)
                if job is not None:
                    questions = Db_Questions.get_role_questions(job.role)
                    questionList = []
                    for question in questions:
                        questionList.append(
                            question.question
                        )

                    return QuestionObject(questions=questionList, role=job.role), 200
                else:
                    self.logger.error("No job present for input id", exc_info=True)
                    return Error(code=404, message="No job present for input id"), 404
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def save_job(self, accept_version, job_request):
        #Db_Jobs().delete()
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                if Db_Questions.get_role_questions(role=job_request.role) is None:
                    self.logger.error("Input role is not defined in questions table", exc_info=True)
                    return Error(code=404, message="No role named: [" + job_request.role + "] is defined in questions table. Please add the role and its questionnaires in questions table first."), 404
                db_jobs_obj = Db_Jobs(
                    id=job_request.id,
                    role=job_request.role,
                    hr_email=job_request.hr_email)
                db_jobs_obj.add()

                return SaveJobObject(message="Job is saved successfully"), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)
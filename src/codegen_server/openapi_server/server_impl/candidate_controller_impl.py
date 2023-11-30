from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_jobs import Db_Jobs
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.dbmodels.db_candidates import Db_Candidates
from openapi_server.models.get_candidate_object import GetCandidateObject

from sqlalchemy import text
from flask import jsonify, make_response

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Candidate_controller_Impl:
    __controller__ = "Candidates"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def get_candidate_questions(self, accept_version, email, login_code):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                candidate = Db_Candidates.get_candidate_by_logincode(login_code)
                if candidate is not None:
                    candidate_name = candidate.name
                    candidate_email = candidate.email
                    candidate_role = ''
                    role_questions = []
                    if candidate_email == email:
                        job = Db_Jobs.get_jobid_deails(candidate.jobid)
                        if job is not None:
                            candidate_role = job.role
                            questions = Db_Questions.get_role_questions(candidate_role)
                            questionList = []
                            if questions is not None:
                                for question in questions:
                                    questionList.append(
                                        question.question
                                    )

                                return GetCandidateObject(
                                    name=candidate_name,
                                    email=candidate_email,
                                    role=candidate_role,
                                    questions=questionList), 200
                            else:
                                self.logger.error("Questions are not set for role: [" + candidate_role + "] in Questions database", exc_info=True)
                            return Error(code=404, message="Questions are not set for role: [" + candidate_role + "] in Questions database"), 404
                        else:
                            self.logger.error("Job id: [" + candidate.jobid + "] data is not present in the Jobs databse", exc_info=True)
                            return Error(code=404, message="Job id: [" + candidate.jobid + "] data is not present in the Jobs databse"), 404
                    else:
                        self.logger.error("No candidate shortlisted with provided email", exc_info=True)
                        return Error(code=404, message="No candidate shortlisted with provided email"), 404
                else:
                    self.logger.error("No candidate present with provided login_code", exc_info=True)
                    return Error(code=404, message="No candidate present with provided login_code"), 404
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex), 500

    @wrap(log_entering, log_exiting)
    def save_candidates(self, accept_version, candidate_request):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                db_candidates_obj = Db_Candidates(
                    name=candidate_request.name,
                    email=candidate_request.email,
                    jobid=candidate_request.jobid
                )

                db_candidates_obj.add()
                return make_response(jsonify({'message': 'Candidate [' + candidate_request.email + '] record saved successfully'})), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex), 500

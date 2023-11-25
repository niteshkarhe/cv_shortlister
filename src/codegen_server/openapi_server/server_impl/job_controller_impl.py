from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_jobs import Db_Jobs
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.models.save_job_object import SaveJobObject

from sqlalchemy import text

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Job_controller_Impl:
    __controller__ = "Job"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def get_questions(self, job_id, accept_version):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                job = Db_Jobs.get_jobid_deails(job_id)
                if job is not None:
                    db.session.execute(text(
                        'select from questions where role=' + str(job.role)
                    ))
                    db.session.commit()
                else:
                    self.logger.error("No job present for input id", exc_info=True)
                return Error(code=404, message="No job present for input id")
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def save_job(self, accept_version, job_request):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                db_jobs_obj = Db_Jobs(role=job_request.role,
                                      hr_email=job_request.hr_email)
                db_jobs_obj.add()

                return SaveJobObject(message="Job is saved successfully")
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)
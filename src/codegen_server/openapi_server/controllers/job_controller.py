import connexion
import six

from openapi_server.models.get_job_object import GetJobObject  # noqa: E501
from openapi_server.models.job_request import JobRequest  # noqa: E501
from openapi_server.models.question_object import QuestionObject  # noqa: E501
from openapi_server.models.save_job_object import SaveJobObject  # noqa: E501
from openapi_server.server_impl.job_controller_impl import Job_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def get_jobid_questions(job_id, accept_version=None):  # noqa: E501
    """To get the question details

    This API is used to get the question details of provided job id # noqa: E501

    :param job_id: 
    :type job_id: str
    :param accept_version: 
    :type accept_version: str

    :rtype: QuestionObject
    """

    impl = serviceImpl()

    return impl.get_jobid_questions(job_id, accept_version)



def get_jobs(accept_version=None, email=None, login_code=None):  # noqa: E501
    """To get the job details

    This API is used to get all job details # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param email: The candidate email
    :type email: str
    :param login_code: The candidate logic_code
    :type login_code: str

    :rtype: GetJobObject
    """

    impl = serviceImpl()

    return impl.get_jobs(accept_version, email, login_code)



def save_job(accept_version=None, job_request=None):  # noqa: E501
    """To store job data for given role

    This API is used to store job data for given role # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param job_request: 
    :type job_request: dict | bytes

    :rtype: SaveJobObject
    """
    if connexion.request.is_json:
        job_request = JobRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.save_job(accept_version, job_request)

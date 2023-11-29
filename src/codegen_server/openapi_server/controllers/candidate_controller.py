import connexion
import six

from openapi_server.models.candidate_request import CandidateRequest  # noqa: E501
from openapi_server.models.get_candidate_object import GetCandidateObject  # noqa: E501
from openapi_server.models.save_candidates200_response import SaveCandidates200Response  # noqa: E501
from openapi_server.server_impl.candidate_controller_impl import Candidate_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def get_candidate_questions(accept_version=None, email=None, login_code=None):  # noqa: E501
    """To get the candidate and question details

    This API is used to get candidate and question details # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param email: The candidate email
    :type email: str
    :param login_code: The candidate logic_code
    :type login_code: int

    :rtype: GetCandidateObject
    """

    impl = serviceImpl()

    return impl.get_candidate_questions(accept_version, email, login_code)



def save_candidates(accept_version=None, candidate_request=None):  # noqa: E501
    """To store candidate data

    This API is used to store shortlisted candidates # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param candidate_request: 
    :type candidate_request: dict | bytes

    :rtype: SaveCandidates200Response
    """
    if connexion.request.is_json:
        candidate_request = CandidateRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.save_candidates(accept_version, candidate_request)

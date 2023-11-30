import connexion
import six

from openapi_server.models.question_object import QuestionObject  # noqa: E501
from openapi_server.models.question_request import QuestionRequest  # noqa: E501
from openapi_server.models.save_question_object import SaveQuestionObject  # noqa: E501
from openapi_server.server_impl.question_controller_impl import Question_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def get_all_questions(accept_version=None):  # noqa: E501
    """To get the question details

    This API is used to get all question details # noqa: E501

    :param accept_version: 
    :type accept_version: str

    :rtype: QuestionObject
    """

    impl = serviceImpl()

    return impl.get_all_questions(accept_version)



def save_questions(accept_version=None, question_request=None):  # noqa: E501
    """To store question data for given role

    This API is used to store questions data for given role # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param question_request: 
    :type question_request: dict | bytes

    :rtype: SaveQuestionObject
    """
    if connexion.request.is_json:
        question_request = QuestionRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.save_questions(accept_version, question_request)



def update_question(accept_version=None, question_request=None):  # noqa: E501
    """To update question data for given role

    This API is used to update question and expected_answer # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param question_request: 
    :type question_request: dict | bytes

    :rtype: SaveQuestionObject
    """
    if connexion.request.is_json:
        question_request = QuestionRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.update_question(accept_version, question_request)

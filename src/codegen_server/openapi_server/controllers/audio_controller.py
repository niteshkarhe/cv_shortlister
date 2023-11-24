import connexion
import six

from openapi_server.models.audio_object import AudioObject  # noqa: E501
from openapi_server.models.audio_request import AudioRequest  # noqa: E501
from openapi_server.server_impl.audio_controller_impl import Audio_controller_Impl as serviceImpl  # noqa: E501
from openapi_server import util




def get_audio(accept_version=None, audio_request=None):  # noqa: E501
    """To capture the audio and convert it to text and store the result

    This API is used to capture audio and convert it to text and then store the result # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param audio_request: 
    :type audio_request: dict | bytes

    :rtype: AudioObject
    """
    if connexion.request.is_json:
        audio_request = AudioRequest.from_dict(connexion.request.get_json())  # noqa: E501

    impl = serviceImpl()

    return impl.get_audio(accept_version, audio_request)



def get_audio_blob(accept_version=None, file=None):  # noqa: E501
    """To capture the audio and convert it to text and store the result

    This API is used to get audio blob and save it and then convert it to text # noqa: E501

    :param accept_version: 
    :type accept_version: str
    :param file: 
    :type file: str

    :rtype: AudioObject
    """

    impl = serviceImpl()

    return impl.get_audio_blob(accept_version, file)

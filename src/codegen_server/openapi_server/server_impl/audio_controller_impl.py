from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils

import speech_recognition as sr
import pyttsx3
import os
from werkzeug.utils import secure_filename
import soundfile
from flask import request
import pydub
from pydub import AudioSegment
import time
import subprocess

from openapi_server.models.error import Error
from openapi_server.config import (
DEFAULT_API_VERSION
)

class Audio_controller_Impl:
    __controller__ = "Audio"
    logger = get_logger()

    @wrap(log_entering, log_exiting)
    def get_audio(self, accept_version, audio_request):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                r = sr.Recognizer()
                while(1):
                    try:
                        with sr.Microphone() as source2:
                            r.adjust_for_ambient_noise(source2, duration=0.2)
                            audio2 = r.listen(source2)
                            MyText = r.recognize_google(audio2)
                            MyText = MyText.lower()

                            self.logger.info('User audio: ' + MyText)
                            Audio_controller_Impl().SpeakText(MyText)
                            return "Did you say " + MyText, 200

                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))

                    except sr.UnknownValueError:
                        print("unknown error occurred")
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def get_audio_blob(self, accept_version, file):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                blobData = request.files['file']
                filename = secure_filename(blobData.filename)
                mpthreepath = os.path.join(os.getcwd() + "\\upload", "audiofile.mp3")
                blobData.save(mpthreepath)
                time.sleep(5)
                wavpath = os.path.join(os.getcwd() + "\\upload", "audiofile.wav")
                subprocess.call(['ffmpeg', '-i', mpthreepath, wavpath])
                #self.logger.info('blob data : ', blobData)

                r = sr.Recognizer()

                with sr.AudioFile(wavpath) as source:
                    audio_data = r.record(source)
                    #text = r.recognize_google(audio_data, language='en-IN', show_all=True)
                    text = r.recognize_google(audio_data)
                    #self.logger.info("Converted text: " + str(text))
                    return_text = " Did you say : " + text
                    # try:
                    #     for num, texts in enumerate(text['alternative']):
                    #         return_text += str(num+1) +") " + texts['transcript']  + " <br> "
                    # except:
                    #     return_text = " Sorry!!!! Voice not Detected "

                return str(return_text), 200
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    def SpeakText(self, command):

        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
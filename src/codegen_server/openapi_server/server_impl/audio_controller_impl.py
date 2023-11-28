from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_users import Db_Users
from openapi_server.dbmodels.db_questions import Db_Questions

from openapi_server.models.audio_object import AudioObject

import speech_recognition as sr
import pyttsx3
import os
from werkzeug.utils import secure_filename
import soundfile
from flask import request
import pydub
from pydub import AudioSegment
import time
from timeit import default_timer as timer
import subprocess
from datetime import datetime;

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
                start = timer()
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
                        end = timer()
                        print(end - start)
                        if (end - start > 10):
                            return Error(code=404, message="No audio detected for more than 10 sec")
                        print("Could not request results; {0}".format(e))

                    except sr.UnknownValueError:
                        end = time.time()
                        print(end - start)
                        if (end - start > 10):
                            return Error(code=404, message="No audio detected for more than 10 sec")
                        print("unknown error occurred")
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    @wrap(log_entering, log_exiting)
    def get_audio_blob(self, accept_version, file):
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                date_format = "%Y-%m-%d %H-%M-%S"
                blobData = request.files['file']
                filename = secure_filename(blobData.filename) + "-" + datetime.utcnow().strftime(date_format)
                recordid = filename[0:filename.index("-")]
                mpfourpath = os.path.join(os.getcwd() + "\\upload", filename+".mp4")
                blobData.save(mpfourpath)
                time.sleep(5)
                wavpath = os.path.join(os.getcwd() + "\\upload", filename+".wav")
                subprocess.call(['ffmpeg', '-i', mpfourpath, wavpath])
                #self.logger.info('blob data : ', blobData)

                r = sr.Recognizer()
                with sr.AudioFile(wavpath) as source:
                    audio_data = r.record(source)
                    start = timer()
                    while(1):
                        try:
                            actual_answer = r.recognize_google(audio_data)
                            userdata = Db_Users.get_userdata_for_given_id(id=recordid)
                            role = ''
                            asked_question = ''
                            if userdata is not None:
                                role = userdata.role
                                asked_question = userdata.question
                            else:
                                return Error(code=404, message="User data could not find with the record id: ["+ recordid + "]"), 404

                            asked_question_details = Db_Questions.get_actual_answer(role=role, question=asked_question)
                            print(asked_question_details.expected_answer)
                            expected_answer = ''
                            if asked_question_details is not None:
                                expected_answer = asked_question_details.expected_answer
                            else:
                                return Error(code=404, message="Question data could not find with the role: ["+ role + "] and question: [" + asked_question + "]"), 404

                            matched_percentage = self.compare_answers(expected_answer, actual_answer)
                            result = ''
                            if matched_percentage == 100:
                                result = 'Passed'
                            else:
                                result = 'Failed'

                            Db_Users().update_userdata_for_given_id(recordid, actual_answer, "\\upload\\"+filename+".mp4", str(matched_percentage), result)

                            return AudioObject(message="For record " + str(recordid) + ", speech to text is: " + actual_answer), 200
                        except sr.UnknownValueError:
                            end = timer()
                            if (end - start > 10):
                                return AudioObject(message="Could not understand audio, unknown error"), 500
                        except sr.RequestError as e:
                            end = timer()
                            if (end - start > 10):
                                return AudioObject(message=str(e)), 500
            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex), 500

    def compare_answers(self, expected_answer, actual_answer):
        expected_answer_words = expected_answer.split()
        actual_answer_words = actual_answer.split()
        flag = []
        for expected in expected_answer_words:
            if expected in actual_answer_words:
                flag.append(True)
            else:
                flag.append(False)

        if all(flag):
            return 100
        else:
            return 0

    def SpeakText(self, command):

        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
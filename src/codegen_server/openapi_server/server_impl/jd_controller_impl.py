import flask
from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_jobs import Db_Jobs
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.models.save_job_object import SaveJobObject

from sqlalchemy import text
from flask import request
from werkzeug.utils import secure_filename
import os
import time
import json
from django.http import HttpResponse
import numpy as np

from datetime import datetime

from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Jd_controller_Impl:
    resume = []
    stopwords2 = []
    resumeText = ''
    resumeWords = ''
    stwords = ''

    __controller__ = "Jd"
    logger = get_logger()
    JD_UPLOAD_DIR = "\\uploaded_jd"
    RESUME_UPLOAD_DIR = "\\uploaded_resume"

    @wrap(log_entering, log_exiting)
    def upload_jd(self, accept_version, file):
        self.logger.info("inside upload jd")
        version_info = utils.get_api_version(accept_version)
        if version_info is None or version_info.lower() == DEFAULT_API_VERSION:
            try:
                # UPLOAD JD
                jdBlobData = request.files["jd"]
                jdfilename = secure_filename(jdBlobData.filename)
                
                self.logger.info("filename = "+ jdfilename)
                now = datetime.now() # current date and time
                date_time = now.strftime("%Y_%m_%d_%H_%M_%S_")
                jdfilename = date_time + jdfilename
                self.logger.info("new filename = "+ jdfilename)

                jdpath = os.path.join(os.getcwd() + self.JD_UPLOAD_DIR, jdfilename)
                jdBlobData.save(jdpath)
                time.sleep(5)

                # UPLOAD RESUMES
                resumeCount = request.form.get('resumecount')
                for i in range(0, int(resumeCount)):
                    resumeBlobData = request.files["resume_"+str(i)]
                    resumefilename = secure_filename(resumeBlobData.filename)
                    self.logger.info("resume filename = "+ resumefilename)
                    resumefilename = date_time + resumefilename
                    self.logger.info("new resume filename = "+ resumefilename)

                    resumepath = os.path.join(os.getcwd() + self.RESUME_UPLOAD_DIR, resumefilename)
                    resumeBlobData.save(resumepath)
                time.sleep(5)

                response = flask.jsonify("success")
                # response.headers.add('Access-Control-Allow-Origin', ['http://localhost:3000', 'http://localhost:8080'])
                return response
                # return HttpResponse(newfilename,content_type="application/json")

            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    def resume_matcher(self):
        pass

    def extractTextFromResume():

        global resume
        global stopwords2
        global resumeText
        global resumeWords
        global stwords

        # Parsing the resume and extracting the text from it

        pdfFileObj = open('resume.pdf', 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[0]
        stwords = set(stopwords.words('english'))

        rawPageText = pageObj.extract_text().replace('\n', '')
        rawPageText = rawPageText.split('  ')
        pageText = []


        for line in rawPageText:

            if len(line) > 0:
                pageText.append(line)


        for line in pageText:

            tokens = sent_tokenize(line)

            for line in tokens:

                if len(line) > 1 and line[0] == ' ': line = line[1:]
                resume.append(line)


        '''
        Load in the list of stopwords
        These are words we do not want to be included in the analysis
        '''

        j = open("stopwords2.txt", "r", encoding="utf8")

        for line in j:
            if len(line) > 1:
                stopwords2.append(line.replace('\n', ''))


        resumeText = ' '.join(map(str, pageText))
        resumeWords = getWordCount(resumeText, 15, '')

        print('\nMost common words in your resume:\n')
        print(resumeWords)
        print()



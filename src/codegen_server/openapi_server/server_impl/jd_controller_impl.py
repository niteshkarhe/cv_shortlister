import flask
from openapi_server.wrappers.wrapper import wrap
from openapi_server.wrappers.standard import log_entering, log_exiting
from openapi_server.app_context import app, db, get_logger
from openapi_server.utils.utilities import utils
from openapi_server.dbmodels.db_jobs import Db_Jobs
from openapi_server.dbmodels.db_questions import Db_Questions
from openapi_server.models.save_job_object import SaveJobObject

# import fitz

from sqlalchemy import text
from flask import request
from werkzeug.utils import secure_filename
import os
import time
import json
import numpy as np
from datetime import datetime
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.corpus import wordnet as wn

import PyPDF2
import numpy as np
import spacy
import collections
import pandas as pd
import re

import requests
from itertools import cycle
import csv
import os
import warnings
from unidecode import unidecode 
import numpy as np
import re 
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


from openapi_server.models.error import Error
from openapi_server.config import (
    DEFAULT_API_VERSION
)

class Jd_controller_Impl:
    warnings.filterwarnings("ignore")
    nlp = spacy.load("en_core_web_lg")

    allData = []
    resume = []
    stopwords2 = []
    resumeText = ''
    resumeWords = ''
    stwords = ''
    bad_chars = ['\n', '\t', '*', "%"]

    lines = []
    words = []
    upper_words = []
    upper_lines = []

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
                newjdfilename = date_time + jdfilename
                self.logger.info("new filename = "+ newjdfilename)

                jdpath = os.path.join(os.getcwd() + self.JD_UPLOAD_DIR, newjdfilename)
                jdBlobData.save(jdpath)
                time.sleep(5)

                # UPLOAD RESUMES
                resumeCount = request.form.get('resumecount')
                final_analysis = {}
                for i in range(0, int(resumeCount)):
                    resumeBlobData = request.files["resume_"+str(i)]
                    resumefilename = secure_filename(resumeBlobData.filename)
                    self.logger.info("resume filename = "+ resumefilename)
                    newresumefilename = date_time + resumefilename
                    self.logger.info("new resume filename = "+ newresumefilename)

                    resumepath = os.path.join(os.getcwd() + self.RESUME_UPLOAD_DIR, newresumefilename)
                    resumeBlobData.save(resumepath)

                    time.sleep(5)
                    self.extractTextFromResume(resumepath)

                    result = self.findResumeMatches(jdfilename, jdpath, newresumefilename.split(".")[0], resumepath)
                    
                    final_analysis[resumefilename.split("-")[0]] = result

                #response = flask.jsonify("success")
                # response.headers.add('Access-Control-Allow-Origin', ['http://localhost:3000', 'http://localhost:8080'])
                #return response
                return final_analysis
                # return HttpResponse(newfilename,content_type="application/json")

            except Exception as ex:
                self.logger.error(ex, exc_info=True)
                return Error(code=500, message=ex)

    def resume_matcher(self):
        pass

    def extractTextFromResume(self, resumePath):

        global resume
        global stopwords2
        global resumeText
        global resumeWords
        global stwords

        # Parsing the resume and extracting the text from it

        pdfFileObj = open(resumePath, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[0]
        self.stwords = set(stopwords.words('english'))

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
                self.resume.append(line)


        '''
        Load in the list of stopwords
        These are words we do not want to be included in the analysis
        '''

        j = open("stopwords2.txt", "r", encoding="utf8")

        for line in j:
            if len(line) > 1:
                self.stopwords2.append(line.replace('\n', ''))


        self.resumeText = ' '.join(map(str, pageText))
        self.resumeWords = self.getWordCount(self.resumeText, 15, '')

        print('\nMost common words in your resume:\n')
        print(self.resumeWords)
        print()

    def findResumeMatches(self, originalJDfilename, jdFileName, resumeFileName, resumepath):

        '''
        Go through the job listings and extract the text that represents the job description
        Calculate the corresponding similarity score to determine how well of a match
        your resume is to that job position
        '''

        print('\nIterating through job postings...\n')
        #csvRows = ['SDET', 'Global Payments', '10.23', 'Pune', 'Key Skills: Automation Automation framework development Java Selenium Rest Assured SQL. Excellent communication skills verbal and written able to communicate with technical people as well as management and business. Has a broad understanding of Software Engineering concepts testing and methodologies. Ability to be flexible accountable reliable and industrious. Establish a strong presence as a change agent providing innovative effective and efficient Quality Assurance practices and solutions. Ability to manage multiple priority efforts in parallel and ensure Quality Assurance standards are followed. Ability to work in an Agile environment. High-energy detail-oriented and proactive with the ability to function under pressure in an independent environment. Required: Fluent in Java and object-oriented development. Strong background in test automation with a focus on APIs. Experience with Spring Framework. Experience REST Assured Apache REST or other service-layer framework. Working experience with JDBC connections Oracle databases and PL/SQL. Experience with JUnit and/or TestNG. Working experience with Selenium WebDriver (Java). Working experience of delivery tools and scripting (Bamboo Jenkins). Working knowledge of ALM tool. Additional Skills. Experience in Pivotal Cloud Foundry or other cloud platforms. Experience and knowledge of continuous delivery and/or continuous integration. Groovy scripting.', 'https://www.google.com']
        #csvRows = ['Key Skills: Automation Automation framework development Java Selenium Rest Assured SQL. Excellent communication skills verbal and written able to communicate with technical people as well as management and business. Has a broad understanding of Software Engineering concepts testing and methodologies. Ability to be flexible accountable reliable and industrious. Establish a strong presence as a change agent providing innovative effective and efficient Quality Assurance practices and solutions. Ability to manage multiple priority efforts in parallel and ensure Quality Assurance standards are followed. Ability to work in an Agile environment. High-energy detail-oriented and proactive with the ability to function under pressure in an independent environment. Required: Fluent in Java and object-oriented development. Strong background in test automation with a focus on APIs. Experience with Spring Framework. Experience REST Assured Apache REST or other service-layer framework. Working experience with JDBC connections Oracle databases and PL/SQL. Experience with JUnit and/or TestNG. Working experience with Selenium WebDriver (Java). Working experience of delivery tools and scripting (Bamboo Jenkins). Working knowledge of ALM tool. Additional Skills. Experience in Pivotal Cloud Foundry or other cloud platforms. Experience and knowledge of continuous delivery and/or continuous integration. Groovy scripting.']
        jdText = self.getJdText(jdFileName)
        csvRows = []
        csvRows.append(jdText)
        try:
            #positionText = csvRows[4].split(". ")
            positionText = csvRows[0].split(". ")

            p = ' '.join(map(str, positionText))
            positionWords = self.getWordCount(p, 15, '')

            keywordSimi = self.getResumeMatchScore(csvRows, self.resume, positionText, self.resumeWords, positionWords)
            recWords = self.recommendKeyWords(positionWords)

            self.allData.append([csvRows[0], keywordSimi, recWords])

            '''
            # Column Names in the excel file
            fields = 'Job Description, KeyWord Similarity, Sentence Similarity, Overall Similarity, Recommended Words\n'

            # Name of Excel file
            now = datetime.now()
            date_time = now.strftime("%Y_%m_%d_%H_%M_%S_")
            fileName = "Resume matcher analysis_" + resumeFileName + "_.csv"
            analysisFilePath = os.path.join(os.getcwd() + self.RESUME_UPLOAD_DIR, fileName)

            #Write to excel file
            MyFile = open(fileName, 'w', encoding="utf-8")

            MyFile.write(fields)

            #Append the data to the rows of the file
            for job in self.allData:
                MyFile.write(self.clean(job[0]) + ',' + str(job[1]) + ',' + str(job[2]) + ',' + str(job[3]) + ',' + self.clean(job[4]))
                MyFile.write('\n')

            MyFile.close()
            '''

            result = {}

            print("resumepath"+ str(resumepath))
            # doc = fitz.open(resumepath)
            # for page in doc:
            #     output = page.get_text("blocks")                   
            #     previous_block_id = 0 # Set a variable to mark the block id
            #     for block in output:
            #         if block[6] == 0: # We only take the text
            #             plain_text = unidecode(block[4])
            #             plain_text = ''.join(i for i in plain_text if not i in bad_chars)
            #             if plain_text != '':
            #                 lines.append(sent_tokenize(plain_text.strip()))
            #                 upper_lines.extend(sent_tokenize(plain_text.upper()))
            #                 words.append(word_tokenize(plain_text))
            #                 upper_words.extend(word_tokenize(plain_text.upper()))

            # for word in words:
            #     candidate_email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', word).group(0)
            #     break


            result["job_id"]=originalJDfilename.split("-")[0]
            result["email"]="nsaudagar1989@gmail.com"
            result["resume_matched_percentage"]=keywordSimi
            # result["experience_matched_percentage"]=sentSimi
            # result["overall_matched"]=overallSimi
            result["recommended_words_in_resume"]=recWords

            return result

        except Exception as ex:
            self.logger.error(ex, exc_info=True)
            return Error(code=500, message=ex)

    def getJdText(self, jdfilename):
        jdpath = os.path.join(os.getcwd() + self.JD_UPLOAD_DIR, jdfilename)
        pdfFileObj = open(jdpath, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[0]

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
                self.resume.append(line)

        jdText = ' '.join(map(str, pageText))
        return jdText

    def getResumeMatchScore(self, job, resume, positionText, resumeWords, positionWords):

        '''
        Key Word Similarity Calculation

        Iterate through the most common words in your resume
        and calculate the similarity scores for each word
        in relation to the most common words in the job description

        Find the max similarity score of each word and calculate
        the average of the scores in the end
        '''

        print()
        print(positionWords)

        overallSimilarity = 0
        maxSims = []

        for i, word in enumerate(resumeWords):

            sims = []

            for j, word2 in enumerate(positionWords):

                sim = self.nlp(resumeWords[i][0]).similarity(self.nlp(positionWords[j][0]))

                if sim == 1: sim = sim * 1.5
                sims.append(sim)

                #print(sim, resumeWords[i][0], positionWords[j][0])

            maxSims.append(max(sims))


        keyWordSimilarity = round(sum(maxSims) / len(maxSims) * 100, 2)
        overallSimilarity = keyWordSimilarity

        print('\nKey Word Similarity:', keyWordSimilarity)


        '''
        Sentence Similarity Calculation
    
        Iterate through each line of your resume and find the sentence 
        that is most similar to it in the job description 
    
        Find the similarity values of the 15 most similar sentences and
        calculate the average of those values 
        '''

        # maxSentSims = []

        # for line in resume:

        #     if len(line) >= 30:

        #         sentSims = []
        #         sents = []

        #         for sent in positionText:

        #             if len(sent) >= 10:

        #                 s = self.sentenceSimilarity(line, sent)
        #                 sentSims.append(s)
        #                 sents.append(line + ' ' + sent)

        #         maxSentSims.append(max(sentSims))


        # maxSentSims.sort(reverse=True)
        # sentSimilarity = round(sum(maxSentSims[0:15]) / len(maxSentSims[0:15]) * 100, 2)

        # overallSimilarity += sentSimilarity


        # print('Sentence Similarity:', sentSimilarity)

        # print('\nOverall Score:', overallSimilarity)
        print()

        return keyWordSimilarity#, sentSimilarity, overallSimilarity

    def recommendKeyWords(self, positionWords):

        '''
        Recommend key words you should add to your resume
        '''

        resumeWordsList = [item for sublist in self.resumeWords for item in sublist if type(item) == str]
        recommendedWords = []

        for word in positionWords:
            if word[0] not in resumeWordsList:
                recommendedWords.append(word[0])

        recWordsStr = ' '.join(map(str, recommendedWords))

        return recWordsStr

    def sentenceSimilarity(self, sentence1, sentence2):

        """ Compute the sentence similarity using Wordnet """

        # Tokenize and tag
        sentence1 = pos_tag(word_tokenize(sentence1))
        sentence2 = pos_tag(word_tokenize(sentence2))

        # Get the synsets for the tagged words
        synsets1 = [self.taggedToSynset(*taggedWord) for taggedWord in sentence1]
        synsets2 = [self.taggedToSynset(*taggedWord) for taggedWord in sentence2]

        # Filter out the Nones
        synsets1 = [ss for ss in synsets1 if ss]
        synsets2 = [ss for ss in synsets2 if ss]

        score, count = 0.0, 0
        best_score = 0

        # For each word in the first sentence
        for synset in synsets1:

            scores = []

            # Get the similarity value of the most similar word in the other sentence
            for ss in synsets2:

                simi = synset.path_similarity(ss)

                if simi != None:
                    scores.append(simi)

            if len(scores) >= 1:
                best_score = max(scores)
                score += best_score
                count += 1

        # Average the values

        if count != 0:
            score /= count
        else:
            score = 0

        return score

    '''
    Key Word Similarity
    Find the most common words in the corpus of text
    '''

    def getWordCount(self, lst, nPrint, companyName):

        # Instantiate a dictionary, and for every word in the file,
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}

        for word in lst.lower().split():

            finalStr = ''

            for c in word:
                if c.isalnum():
                    finalStr += c

            if finalStr not in self.stwords and finalStr not in self.stopwords2 and len(finalStr) > 3 and finalStr != companyName:

                if finalStr not in wordcount:
                    wordcount[finalStr] = 1

                else:
                    wordcount[finalStr] += 1


        word_counter = collections.Counter(wordcount)


        lst = word_counter.most_common(nPrint)
        df = pd.DataFrame(lst, columns = ['Word', 'Count'])
        #df.plot.bar(x = 'Word', y = 'Count')

        return lst

    def clean(self, stng):

        # We want to get rid of these characters
        bad_chars = ['[', ']', '"', ',']

        for i in bad_chars :
            stng = stng.replace(i, '')

        return stng

    def pennToWn(self, tag):

        # Convert between a Penn Treebank tag to a simplified Wordnet tag

        if tag.startswith('N'):
            return 'n'

        if tag.startswith('V'):
            return 'v'

        if tag.startswith('J'):
            return 'a'

        if tag.startswith('R'):
            return 'r'

        return None


    def taggedToSynset(self, word, tag):

        wn_tag = self.pennToWn(tag)

        if wn_tag is None:
            return None

        try:
            return wn.synsets(word, wn_tag)[0]
        except:
            return None
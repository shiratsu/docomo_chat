# -*- coding: utf-8 -*-
from lib.conversationAnalysis import ConversationAnalysis
from lib.docomoConversationAPI import DocomoConversationAPI
from config.config import Config
import json

class TestConversationAnalysis(ConversationAnalysis):

    def __init__(self):
        self.config = Config()
        self.convHandle = DocomoConversationAPI()
        self.url = ''


    # 文章解析用のURLを作成
    def makeSentenceAnalysisUrl(self):
        # configから設定を取得
        urlBase = self.config.read('docomo','url') 
        apiKey = self.config.read('docomo','api_key') 
        # urlを設定
        self.url = urlBase+apiKey



    # 文章解析
    def sentenceAnalysis(self,sent,workType):

        # パラメータを作成
        param = {"sentence" : sent,"info_filter" : "form"}
        objJson = self.convHandle.makeParamJson(param)

        responseBody = self.convHandle.sendJsonRequest(self.url,objJson)

        # response結果を確認
        self.checkJsonResponse(responseBody)
       
    # jsonレスポンス解析
    def checkJsonResponse(self,objJson):

        returnObj = ''

        resultObjs = json.loads(objJson.split('\n')[0])
        for resultObj in resultObjs["ne_list"]:
             returnObj = resultObj

        return returnObj

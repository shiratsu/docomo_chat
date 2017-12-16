# -*- coding: utf-8 -*-
from lib.conversationAnalysis import ConversationAnalysis
from lib.docomoConversationAPI import DocomoConversationAPI
from config.config import Config


class TestConversationAnalysis(ConversationAnalysis):

    def __init__(self):
        self.config = Config()
        self.url = ''


    # 文章解析用のURLを作成
    def makeSentenceAnalysisUrl(self):
        # configから設定を取得
        urlBase = config.read('docomo','url') 
        apiKey = config.read('docomo','api_key') 
        # urlを設定
        self.url = urlBase+apiKey



    # 文章解析
    def sentenceAnalysis(self,sent):

        # パラメータを作成
        param = {"sentence" : sent,"info_filter" : "form"}
        objJson = convHandle.makeParamJson(param)

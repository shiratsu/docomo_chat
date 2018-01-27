
# -*- coding: utf-8 -*-
from lib.conversationAnalysis import ConversationAnalysis
from lib.docomoConversationAPI import DocomoConversationAPI
from config.config import Config
import json

class ShiftConversationAnalysis(ConversationAnalysis):

    # 初期化
    def __init__(self):
        super(ShiftConversationAnalysis, self).__init__()
        self.dicAnalysis = {'PERSON':'','EMAIL':'','WORKID':''}
        self.analysisCompFlag = False

    # 言語解析処理
    def sentenceAnalysis(self,sent):

        # まずは名前
        if self.dicAnalysis['PERSON'] == None:
            strName = self.getPerson(sent)
            if strName != None:
                self.dicAnalysis['PERSON'] = strName

        
        # 次はワークID
        if self.dicAnalysis['WORKID'] == None:
            strId = self.getWorkId(sent)
            if strId != None:
                self.dicAnalysis['WORKID'] = strName

# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import MeCab
import re

class ConversationAnalysis(metaclass=ABCMeta):

    def __init__(self):
        self.mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.mecab.parse('')


    @abstractmethod
    def sentenceAnalysis(self,sent):
        pass

    # 文章から人名を取得(mecabで解析して取得する。)
    def getPerson(self,sent):
        node = self.mecab.parseToNode(sent)
        aryName = []
        while node:
            #品詞を取得
            pos1 = node.feature.split(",")[1]
            pos2 = node.feature.split(",")[2]
            pos3 = node.feature.split(",")[3]
            if pos1 == '名詞' and pos2 == '固有名詞':
                #単語を取得
                word = node.surface
                aryName.append(word)
            else:
                continue
            
        strName = ''.join(str_list)
        return strName


    @abstractmethod
    def getDate(self,sent):
        pass

    @abstractmethod
    def getTime(self,sent):
        pass

    # 正規表現を使ってメアドのパターンを取得
    def getEmail(self,sent):
        strPattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+'
        objRe = re.compile(strPattern)
        return objRe.match(sent)

    @abstractmethod
    def getLocate(self,sent):
        pass

    @abstractmethod
    def getJobKind(self,sent):
        pass

    @abstractmethod
    def getDistance(self,sent):
        pass

    @abstractmethod
    def getMoney(self,sent):
        pass

    @abstractmethod
    def getOther(self,sent):
        pass

    @abstractmethod
    def getDeny(self,sent):
        pass

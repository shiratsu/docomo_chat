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
    # katakanaで入れられた場合は、今のところ判定不可
    def getPerson(self,sent):
        node = self.mecab.parse(sent)
        aryName = []
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            pos1 = features[0]
            pos2 = features[1]
            pos3 = features[2]
            if pos1 == '名詞' and pos2 == '固有名詞' and pos3 == '人名':
                #単語を取得
                word = surface
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
    
    # 電話番号を取得
    # 電話番号は複数パターンある
    def getPhoneNumber(self,sent):
        aryReturn = []
        
        strPattern1 = '^\d{10}$|^\d{11}$'
        objRe1 = re.compile(strPattern1)
        aryReturn = objRe1.match(sent)
        
        strPattern2 = '^\d{2,4}-\d{2,4}-\d{4}$'
        objRe2 = re.compile(strPattern2)
        aryReturn = objRe2.match(sent)
        
        return aryReturn

    # 地名
    # ベースは形態素解析で良い気がする
    def getLocate(self,sent):
        strLoc = ''
        aryName = []
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            pos1 = features[0]
            pos2 = features[1]
            pos3 = features[2]
            if pos1 == '名詞' and pos2 == '固有名詞' and pos3 in [ '地域','一般','組織']:
                #単語を取得
                word = surface
                aryName.append(word)
            else:
                continue
            
        strLoc = ''.join(str_list)

        return strLoc

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

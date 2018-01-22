# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class ConversationAnalysis(metaclass=ABCMeta):

    @abstractmethod
    def sentenceAnalysis(self,sent):
        pass

    @abstractmethod
    def getPerson(self,sent):
        pass

    @abstractmethod
    def getDate(self,sent):
        pass

    @abstractmethod
    def getTime(self,sent):
        pass

    @abstractmethod
    def getEmail(self,sent):
        pass

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

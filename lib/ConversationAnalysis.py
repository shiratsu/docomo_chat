# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class ConversationAnalytics(metaclass=ABCMeta):

    @abstractmethod
    def sentenceAnalysis(self,sent):
        pass


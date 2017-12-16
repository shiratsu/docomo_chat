# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class ConversationAnalysis(metaclass=ABCMeta):

    @abstractmethod
    def sentenceAnalysis(self,sent):
        pass


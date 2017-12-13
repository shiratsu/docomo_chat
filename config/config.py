# -*- coding: utf-8 -*-
import configparser
import os,sys

class Config(object):
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath(os.path.dirname(__file__))+'/config.ini')

    # keyに該当する定義を読む
    def read(self,key1,key2):
        return self.config[key1][key2]

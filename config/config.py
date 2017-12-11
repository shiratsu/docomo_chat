# -*- coding: utf-8 -*-
import configparser
import os,sys

class Config(object):
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath(os.path.dirname(__file__))+'/config.ini')
        print('docomo' in self.config)

    # keyに該当する定義を読む
    def read(self,key1,key2):
        print(self.config)
        return self.config[key1][key2]

# -*- coding: utf-8 -*-
import configparser

class Config(object):
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        config.read('config.txt')

    # keyに該当する定義を読む
    def read(self,key1,key2):
        return config[key1][key2]

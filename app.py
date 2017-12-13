# -*- coding: utf-8 -*-
from lib.testConversationHandle import TestConversationHandle
from config.config import Config
import json

if __name__ == '__main__':
    
    config = Config()
    convHandle = TestConversationHandle()

    print('S: こんにちは！お名前を教えてください。')
    while True:
        # input from User
        sent = input('U: ')
        if sent == 'ありがとう' or sent == 'Thanks' or sent == 'Thank you' or sent == 'ありがと':
            print('S: どういたしまして')
            break

        convHandle.sentenceAnalysis(sent)

        resultObjs = json.loads(responseBody.split('\n')[0])

        for resultObj in resultObjs["ne_list"]:
            print(resultObj)

        break


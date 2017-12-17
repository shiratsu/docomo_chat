# -*- coding: utf-8 -*-
from lib.testConversationAnalysis import TestConversationAnalysis

if __name__ == '__main__':
    
    convObj = TestConversationAnalysis()

    print('S: こんにちは！お名前を教えてください。')
    while True:
        # input from User
        sent = input('U: ')
        if sent == 'ありがとう' or sent == 'Thanks' or sent == 'Thank you' or sent == 'ありがと':
            print('S: どういたしまして')
            break

        #URLを初期化しておく
        convObj.makeSentenceAnalysisUrl()

        # sentence解析
        analysisResult = convObj.sentenceAnalysis(sent)

        #resultObjs = json.loads(responseBody.split('\n')[0])

        #for resultObj in resultObjs["ne_list"]:
        #    print(resultObj)

        #break


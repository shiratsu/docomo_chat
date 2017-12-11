# -*- coding: utf-8 -*-
from lib.conversationHandle import ConversationHandle
from config.config import Config

if __name__ == '__main__':
    
    config = Config()
    convHandle = ConversationHandle()

    print('S: こんにちは！お名前とお電話番号を教えてください。')
    while True:
        # input from User
        sent = input('U: ')
        if sent == 'ありがとう' or sent == 'Thanks' or sent == 'Thank you' or sent == 'ありがと':
            print('S: どういたしまして')
            break

        # configから設定を取得
        urlBase = config.read('docomo','url') 
        apiKey = config.read('docomo','api_key') 
        
        # urlを設定
        url = urlBase+apiKey

	# パラメータを作成
        param = {"sentence" : sent,"info_filter" : "form"}
        objJson = convHandle.makeParamJson(param) 

	# 送信
        responseBody = convHandle.sendJsonRequest(url,objJson)
	
        print(responseBody)


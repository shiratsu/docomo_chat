# -*- coding: utf-8 -*-
import urllib.request, json
import configparser

class ConversationHandle(object):
	
    def __init__(self):

    # jsonパラメータを作成    
    def makeParamJson(self,param):
        jsonStr = json.dumps(param)
        return jsonStr

    def sendJsonRequest(self,url,jsonStr):

    # リクエストを送信する
    def sendGetRequest(self,url,param):
        strParam = "&".join(param)
        response = requests.get(url+"&"+strParam)
        print(response.status_code)    # HTTPのステータスコード取得
        print(response.text)    # レスポンスのHTMLを文字列で取得		
		

# -*- coding: utf-8 -*-
import urllib.request, json
import configparser

class ConversationHandle(object):
	
    #def __init__(self):

    # jsonパラメータを作成    
    def makeParamJson(self,param):
        jsonStr = json.dumps(param).encode("utf-8")
        return jsonStr

    # jsonを送信する
    def sendJsonRequest(self,url,jsonData):
        method = "POST"
        headers = {"Content-Type" : "application/json"}
        print(url)
        print(jsonData)
    	# httpリクエストを準備してPOST
        request = urllib.request.Request(url, data=jsonData, method=method, headers=headers)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

        return response_body 

    # リクエストを送信する
    def sendGetRequest(self,url,param):
        strParam = "&".join(param)
        response = requests.get(url+"&"+strParam)
        print(response.status_code)    # HTTPのステータスコード取得
        print(response.text)    # レスポンスのHTMLを文字列で取得		
		

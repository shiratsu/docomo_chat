# -*- coding: utf-8 -*-
#
# trainningデータの作成
#
import os

jobList = []
jobSentenceList = []
locationList = []
locationSentenceList = []

with open('job_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        jobList.append(strLine)

with open('location_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        locationList.append(strLine)


with open('job.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # JOBを置換
        for job in jobList:
            strText = strLine.replace('JOB',job)
            jobSentenceList.append(strText)

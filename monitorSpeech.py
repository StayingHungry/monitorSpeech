# -*- coding: utf-8 -*-
from flask import Flask
import requests
import json
app = Flask(__name__)
url = "http://fanyi.sogou.com/reventondc/synthesis"
# url = "http://10.153.49.142/reventondc/synthesis"

querystring10 = {"text":"china","speed":"1","lang":"en","from":"pagetest"}
querystring1 = {"text":"china%20is%20a%20country!","speed":"1","lang":"en","from":"pagetest"}
querystring2 = {"text":"a%20book%20of%20selected%20poems","speed":"1","lang":"en","from":"pagetest"}
querystring3 = {"text":"she%20felt%20every%20emotion%20in%20the%20book%20of%20love","speed":"1","lang":"en","from":"pagetest"}
querystring4 = {"text":"Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army%20Chinese%20people%27s%20liberation%20army","speed":"1","lang":"en","from":"pagetest"}

querystring5 = {"text":"%e4%b8%ad%e5%9b%bd%e6%98%af%e4%b8%80%e4%b8%aa%e5%9b%bd%e5%ae%b6","speed":"1","lang":"zh-CHS","from":"pagetest"}
querystring6 = {"text":"%e4%b8%ad","speed":"1","lang":"zh-CHS","from":"pagetest"}
querystring7 = {"text":"%e4%b8%ad%e5%ae%b6","speed":"1","lang":"zh-CHS","from":"pagetest"}
querystring8 = {"text":"%e4%b8%ad%e6%98%af%e4%b8%80%e4%b8%aa%e5%9b%bd%e5%ae%b6","speed":"1","lang":"zh-CHS","from":"pagetest"}
querystring9 = {"text":"%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be%e8%9c%80%e9%81%93%e9%9a%be","speed":"1","lang":"zh-CHS","from":"pagetest"}
querystringList = []
for i in range(1,11):
    nameTem = "querystring" + str(i)
    querystringList.append(eval(nameTem))
headers = {
    'cache-control': "no-cache",
    'postman-token': "da658e0e-076c-329d-8def-9b0fa50d0d8b"
    }

@app.route('/monitorSpeech')
def hello_world():
    dictResult = {}
    rightNum = 0
    for i, item in enumerate(querystringList):
        responseTem = requests.request("GET", url, headers=headers, params=item)
        # print type(responseTem.headers)
        jsonHeader = json.dumps((dict(responseTem.headers)))
        dictHeader = json.loads(jsonHeader)
        dictResult['querystring' + str(i)] = dictHeader
        # print type(dictHeader)
        if "'Content-Type': 'audio/mpeg" in str(responseTem.headers):
            rightNum = rightNum + 1
        # print str( "'Content-Type': 'audio/mpeg" in str(responseTem.headers)) + "----------------------------------" + str(responseTem.headers) + "-----------" + str(responseTem.status_code)
    # return 'Hello World!'
    rightRate = (rightNum + 0.0) /len(querystringList) * 100
    # print str(rightRate) + '%'
    dictResult['rightRate'] = str(rightRate) + '%'
    dictResult['rightNum'] = rightNum
    return json.dumps(dictResult)


if __name__ == '__main__':
    app.run(host="10.129.152.64",port=8187,debug=True)

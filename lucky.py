import requests as req
import xmltodict as xml
import json
import pprint


url = 'http://localhost:9000/receive'
resGet = req.get(url)
#print(resGet.text)

dicGet = json.loads(resGet.text)
#print(dicGet)

dumpsGet = json.dumps(dicGet, indent=4)
#print(dumpsGet)

resPost = req.post(url)
#print(resPost.text)

dicPost = json.loads(resPost.text)
#print(dicPost)

dumpsPost = json.dumps(dicPost, sort_keys = False)
#print(dumpsPost)

publicUrl = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc'
params = {'ServiceKey':'LRiceR8zAlFFqPkIOt8aKIXR0Qw4Q9N0gaCcBFBreTur%2B4vXpeEBFt7RkoaNh52I83Zp43kJe4to3zwTYMm6GQ%3D%3D', 'pageNo':'1', 'numOfRows':'5', 'year':'2019', 'itemCode':'PM10'}
publicGet = req.get(publicUrl, params=params)
publicParse = xml.parse(publicGet.text)

print(publicGet)
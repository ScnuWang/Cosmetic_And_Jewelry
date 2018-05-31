import requests
import json
from urllib import request
from urllib import parse
from urllib.request import urlopen

# 网站地址
website_url = "https://www.swarovski.com"
# url = "https://www.swarovski.com/Web_DE/de/json/json-result?SearchParameter=%26%40QueryTerm%3DCEP_WatchFW17_TimelessStyle_campaign%26CategoryUUIDLevelX%3DB8kKaSUCmAEAAAEnLNBToUKM%26CategoryUUIDLevelX%252FB8kKaSUCmAEAAAEnLNBToUKM%3DBMQKaVgfJWEAAAFjvvF6fYwv%26%40Page%3D1&PageSize=12&View=M"
values = {'SearchParameter':'&@QueryTerm=CEP_WatchFW17_TimelessStyle_campaign&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=BMQKaVgfJWEAAAFjvvF6fYwv&@Page=1','PageSize':12,'View':'M'}
url = "https://www.swarovski.com/Web_DE/de/json/json-result?"
data = parse.urlencode(values)
print(url+data)
url_encode = url+data
print(url_encode)
response = requests.get(url_encode)

print(response.text)

response_json = json.loads(response.text)

print(response_json['SearchResult']['PageSize'])
print(response_json['SearchResult']['PageCount'])
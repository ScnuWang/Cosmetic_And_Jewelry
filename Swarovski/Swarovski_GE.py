import requests
# 网站地址
website_url = "https://www.swarovski.com"

url = "https://www.swarovski.com/Web_DE/de/json/json-result?SearchParameter=%26%40QueryTerm%3DCEP_WatchFW17_TimelessStyle_campaign%26CategoryUUIDLevelX%3DB8kKaSUCmAEAAAEnLNBToUKM%26CategoryUUIDLevelX%252FB8kKaSUCmAEAAAEnLNBToUKM%3DBMQKaVgfJWEAAAFjvvF6fYwv%26%40Page%3D1&PageSize=12&View=M"


response = requests.get(url)

print(response.text)
import time
import requests

i = 0
while i < 10:
    response = requests.get("https://www.swarovski.com.cn/Web_CN/en/json/json-result?SearchParameter=&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&@Sort.FFSort=0&@Page=1&PageSize=48&View=M").text
    print(response)
    if response:
        break
    i += 1
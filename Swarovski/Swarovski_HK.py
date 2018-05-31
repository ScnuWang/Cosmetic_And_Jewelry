import requests
import pymysql
import json

# 网站地址
website_url = "https://www.swarovski.com/Web_HK/zh/index"
# url = "https://www.swarovski.com/Web_HK/zh/json/json-result?SearchParameter=&@QueryTerm=CEP_WatchFW17_TimelessStyle_campaign&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%252FB8kKaSUCmAEAAAEnLNBToUKM=BMQKaVgfJWEAAAFjvvF6fYwv&@Page=1&PageSize=12&View=M"
url = "https://www.swarovski.com/Web_HK/zh/json/json-result?SearchParameter=&@QueryTerm=CEP_WatchFW17_TimelessStyle_campaign&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=BMQKaVgfJWEAAAFjvvF6fYwv&@Page=1&PageSize=12&View=M"

response = requests.get(url)
print(response.text)

response_json = json.loads(response.text)

print(response_json['SearchResult']['PageSize'])
print(response_json['SearchResult']['PageCount'])

# 获取数据库连接
db = pymysql.connect("localhost","root","admin","data")
# 创建一个游标对象
cursor = db.cursor()
# 执行sql查询
cursor.execute("Select version()")
# 使用fetchone()获取单条记录
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库
db.close()
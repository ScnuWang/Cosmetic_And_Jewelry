import requests
import pymysql

# 网站地址
website_url = "https://www.swarovski.com/Web_HK/zh/index"
url = "https://www.swarovski.com/Web_DE/de/json/json-result?SearchParameter=%26%40QueryTerm%3DCEP_WatchFW17_TimelessStyle_campaign%26CategoryUUIDLevelX%3DB8kKaSUCmAEAAAEnLNBToUKM%26CategoryUUIDLevelX%252FB8kKaSUCmAEAAAEnLNBToUKM%3DBMQKaVgfJWEAAAFjvvF6fYwv%26%40Page%3D1&PageSize=12&View=M"
response = requests.get(url)
print(response.text)

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
import requests
import json
import pymysql
import re
import time
import os
from urllib import parse


#  项链

# 构建请求地址

        # 德国
website_url = "https://www.swarovski.com"
url = "https://www.swarovski.com/Web_DE/en/json/json-result?"
query_term = "&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=aZkKaVgf510AAAFjw_F6fYwv&@Sort.FFSort=0&@Page=1"


# 组装请求地址
def encode_url(url, query_term, page_count):
    query_term = query_term + str(page_count)
    prarms = {'SearchParameter':query_term,'PageSize':48,'View':'M'}
    encode_prarms = parse.urlencode(prarms)
    url_encode = url+encode_prarms
    return url_encode


# 获取产品总页数
page_count = 1
response = json.loads(requests.get(encode_url(url,query_term,page_count)).text)
# print(response['SearchResult']['PageCount'])

# 保存数据至是数据库

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='data', charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 解析数据
total_count = response['SearchResult']['PageCount']
while page_count <= total_count:
    request_url = encode_url(url,query_term,page_count)
    response = requests.get(request_url).text
    response_json = json.loads(response)

    # 保存数据为文件
    file_time = time.strftime("%Y%m%d", time.localtime())
    # 文件名组成部分：品牌名称+ 时间 + 地点 + 分类 + 页数
    fileName = str(1) + '_' + str(file_time) + '_' + str(3) + '_' + str(1) + '_' + str(page_count) + '.json'

    # 判断文件夹是否存在，不存在的话就新建文件夹
    path = '../data'
    if not os.path.exists(path) :
        os.mkdir(path)
    f = open('../data/'+fileName, 'a+', encoding='utf-8')
    f.write(response)
    f.close()

    products = response_json['SearchResult']['Products']
    # print(products)
    for product in products:
        # print(product)
        original_id = product['SKU']
        # print(original_id)
        brand_id = 1
        sales_location = 3
        product_name = product['Name']
        product_price = int(re.sub('\D',"",product['Price']))/100
        original_currency = re.sub(r'[^A-Z]', '', product['Price'])
        product_url = product['DetailPage']
        product_image = website_url + product['ProductImage']
        product_thumbnail = website_url + product['Thumbnail']
        if product['OldPrice'] == "":
            old_price = 0.00
        else:
            old_price = int(re.sub('\D',"",product['OldPrice']))/100
        nick_name = ""
        cny_product_price = 0.00
        cny_exchange_rate = 0.00
        product_status = 1 # 1：在售；2：下架；3新上；4：异常
        category_id = 1
        update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        try:
            # 执行sql语句
            # cursor.executemany()
            cursor.execute("INSERT INTO cj_product(original_id,brand_id,sales_location,product_name,product_price,original_currency, product_url,product_image,product_thumbnail,old_price,nick_name,cny_product_price,cny_exchange_rate,product_status,category_id,update_time)VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');" .format(original_id,brand_id,sales_location,product_name,product_price,original_currency, product_url,product_image,product_thumbnail,old_price,nick_name,cny_product_price,cny_exchange_rate,product_status,category_id,update_time))
            # 提交到数据库执行
            db.commit()
        except BaseException  as err:
            # 如果发生错误则回滚
            print(err)
            db.rollback()
    page_count += 1

# 关闭数据库连接
db.close()
import requests
import json
import pymysql
import re
import time
import os
from urllib import parse


# 一个地域的所有分类

# 组装请求地址
def encode_url(url, query_term, page_count):
    query_term = query_term + str(page_count)
    prarms = {'SearchParameter': query_term, 'PageSize': 48, 'View': 'M'}
    encode_prarms = parse.urlencode(prarms)
    url_encode = url + encode_prarms
    return url_encode


def all(website_url, url, query_term, sales_location, category_id):
    # 获取产品总页数
    page_count = 1
    response = json.loads(requests.get(encode_url(url, query_term, page_count)).text)
    # print(response['SearchResult']['PageCount'])

    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='data', charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 解析数据
    total_count = response['SearchResult']['PageCount']
    while page_count <= total_count:
        request_url = encode_url(url, query_term, page_count)
        response = requests.get(request_url).text
        response_json = json.loads(response)

        # 保存数据为文件
        file_time = time.strftime("%Y%m%d", time.localtime())
        # 文件名组成部分：品牌名称+ 时间 + 地点 + 分类 + 页数
        fileName = str(1) + '_' + str(file_time) + '_' + str(1) + '_' + str(sales_location) + '_' + str(
            page_count) + '.json'

        # 判断文件夹是否存在，不存在的话就新建文件夹
        path = 'data'
        if not os.path.exists(path):
            os.mkdir(path)
        f = open('data/' + fileName, 'a+', encoding='utf-8')
        f.write(response)
        f.close()

        products = response_json['SearchResult']['Products']
        # print(products)
        for product in products:
            # print(product)
            original_id = product['SKU']
            # print(original_id)
            brand_id = 1
            # sales_location = 1
            product_name = product['Name']
            product_price = int(re.sub('\D', "", product['Price'])) / 100
            original_currency = re.sub(r'[^A-Z]', '', product['Price'])
            product_url = product['DetailPage']
            product_image = website_url + product['ProductImage']
            product_thumbnail = website_url + product['Thumbnail']
            if product['OldPrice'] == "":
                old_price = 0.00
            else:
                old_price = int(re.sub('\D', "", product['OldPrice'])) / 100
            nick_name = ""
            cny_product_price = 0.00
            cny_exchange_rate = 0.00
            product_status = 1  # 1：在售；2：下架；3新上；4：异常
            # category_id = 1
            update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            try:
                # 执行sql语句
                # 保存数据至是数据库
                cursor.execute(
                    "INSERT INTO cj_product(original_id,brand_id,sales_location,product_name,product_price,original_currency, product_url,product_image,product_thumbnail,old_price,nick_name,cny_product_price,cny_exchange_rate,product_status,category_id,update_time)VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
                        original_id, brand_id, sales_location, product_name, product_price, original_currency,
                        product_url, product_image, product_thumbnail, old_price, nick_name, cny_product_price,
                        cny_exchange_rate, product_status, category_id, update_time))
                # 提交到数据库执行
                db.commit()
            except BaseException  as err:
                # 如果发生错误则回滚
                print(err)
                db.rollback()
        page_count += 1

    # 关闭数据库连接
    db.close()


query_term_cn = {
    1: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=8E8KaVgfTQYAAAFjiwl6fYzt&@Sort.FFSort=0&@Page=',
    2: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=VXYKaVgfeAEAAAFjigl6fYzt&@Sort.FFSort=0&@Page=',
    3: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=OhUKaVgfd_8AAAFjigl6fYzt&@Sort.FFSort=0&@Page=',
    4: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=csIKaVgfNbsAAAFjjAl6fYzt&@Sort.FFSort=0&@Page=',
    5: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=Z28KaVgfU2AAAAFjiQl6fYzt&@Sort.FFSort=0&@Page=',
    6: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=K3IKaVgfd_0AAAFjigl6fYzt&@Sort.FFSort=0&@Page=',
    7: '&@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=OAQKaVgfNbkAAAFjjAl6fYzt&@Sort.FFSort=0&@Page=',
    8: '@QueryTerm=*&CategoryUUIDLevelX=tfYKaSUCEOsAAAEn_NtToUKM&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM=EjEKaVgfTq0AAAFjMgl6fYzt&CategoryUUIDLevelX%2FtfYKaSUCEOsAAAEn_NtToUKM%2FEjEKaVgfTq0AAAFjMgl6fYzt=QG8KaVgfTqsAAAFjMgl6fYzt&@Sort.FFSort=0&@Page='}
query_term_hk = {
    1: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=xxcKaVgfHFgAAAFjvtt6fYxb&@Sort.FFSort=0&@Page=',
    2: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=GSkKaVgfEYwAAAFj0tt6fYxb&@Sort.FFSort=0&@Page=',
    3: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=mQUKaVgfEYoAAAFj0tt6fYxb&@Sort.FFSort=0&@Page=',
    4: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=IsMKaVgf6IwAAAFjvdt6fYxb&@Sort.FFSort=0&@Page=',
    5: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=a2AKaVgfcO8AAAFj0dt6fYxb&@Sort.FFSort=0&@Page=',
    6: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=JisKaVgfEYgAAAFj0tt6fYxb&@Sort.FFSort=0&@Page=',
    7: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=6MQKaVgfEY4AAAFj0tt6fYxb&@Sort.FFSort=0&@Page=',
    8: '&@QueryTerm=*&CategoryUUIDLevelX=fQcKaSUCzHcAAAEnktxToUKM&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM=fk0KaVgfKRcAAAFjv9t6fYxb&CategoryUUIDLevelX%2FfQcKaSUCzHcAAAEnktxToUKM%2Ffk0KaVgfKRcAAAFjv9t6fYxb=9hIKaVgfHFkAAAFjvtt6fYxb&@Sort.FFSort=0&@Page='}
query_term_ge = {
    1: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=aZkKaVgf510AAAFjw_F6fYwv&@Sort.FFSort=0&@Page=',
    2: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=UOUKaVgfAgYAAAFjwfF6fYwv&@Sort.FFSort=0&@Page=',
    3: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=jCQKaVgf.bQAAAFjwvF6fYwv&@Sort.FFSort=0&@Page=',
    4: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=uL0KaVgfQ1cAAAFjlPF6fYwv&@Sort.FFSort=0&@Page=',
    5: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=FscKaVgfG1UAAAFjwPF6fYwv&@Sort.FFSort=0&@Page=',
    6: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=pu4KaVgfAgQAAAFjwfF6fYwv&@Sort.FFSort=0&@Page=',
    7: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=nbgKaVgf.bgAAAFjwvF6fYwv&@Sort.FFSort=0&@Page=',
    8: '&@QueryTerm=*&CategoryUUIDLevelX=B8kKaSUCmAEAAAEnLNBToUKM&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM=KdcKaVgfUt4AAAFjkPF6fYwv&CategoryUUIDLevelX%2FB8kKaSUCmAEAAAEnLNBToUKM%2FKdcKaVgfUt4AAAFjkPF6fYwv=1lEKaVgf.bYAAAFjwvF6fYwv&@Sort.FFSort=0&@Page='}

website_url = {'cn': 'https://www.swarovski.com.cn', 'hk': 'https://www.swarovski.com',
               'ge': 'https://www.swarovski.com'}
url = {'cn': 'https://www.swarovski.com.cn/Web_CN/en/json/json-result?',
       'hk': 'https://www.swarovski.com/Web_HK/en/json/json-result?',
       'ge': 'https://www.swarovski.com/Web_DE/en/json/json-result?'}
query_term = {'cn': query_term_cn, 'hk': query_term_hk, 'ge': query_term_ge}
sales_location = {'cn': 1, 'hk': 2, 'ge': 3}


# 按所有的区域数量确定最外层循环次数
count = 1
for location in [k for k in sales_location.keys()]:
    website_url = website_url[location]
    url = url[location]
    location_id = sales_location[location]



all(website_url, url, query_term, 3, 3)
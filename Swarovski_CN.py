import requests
from bs4 import BeautifulSoup

# 网站地址
website_url = "https://www.swarovski.com.cn/Web_CN/zh/index"


# 项链列表页地址
url = "https://www.swarovski.com.cn/Web_CN/zh/0108/category/%E9%A6%96%E9%A5%B0_/%E9%A1%B9%E9%93%BE.html"

response = requests.get(url).text
# print(response.text)

soup = BeautifulSoup(response)

productlist = soup.select('.listproduct')
# print(len(productlist))

for product in productlist :
    # print(product)
    # 解析产品的编号
    product_id = product['gtm-product-sku']
    # print(product_id)
    # 解析产品的Url
    product_detail_url = product.select('a')[0]['href']
    # print(product_url)
    # 解析产品列表页的图片地址 图片大小180 * 180
    # print(product.select('a img')[0]) # 获取产品图片元素
    product_img_url = website_url + product.select('a img')[0]['src']
    # print(product_img_url)
    # 解析产品的中文名称
    product_nickname = product.select('a img')[0]['alt']
    # print(product_nickname)



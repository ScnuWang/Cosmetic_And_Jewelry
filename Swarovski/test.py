import requests

url = "https://www.swarovski.com.cn/Web_CN/zh/json/json-result?SearchParameter=%26%40QueryTerm%3D*%26CategoryUUIDLevelX%3DtfYKaSUCEOsAAAEn_NtToUKM%26CategoryUUIDLevelX%252FtfYKaSUCEOsAAAEn_NtToUKM%3DEjEKaVgfTq0AAAFjMgl6fYzt%26CategoryUUIDLevelX%252FtfYKaSUCEOsAAAEn_NtToUKM%252FEjEKaVgfTq0AAAFjMgl6fYzt%3D8E8KaVgfTQYAAAFjiwl6fYzt%26%40Sort.FFSort%3D0%26%40Page%3D3&PageSize=36&View=M"

response = requests.get(url)
print(response.text)
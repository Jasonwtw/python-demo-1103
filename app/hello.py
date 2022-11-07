import requests

url = 'http://www.baidu.com'
rep = requests.get(url)
print(rep.url)
print('hello python!')
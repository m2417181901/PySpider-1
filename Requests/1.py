import requests
url2 = 'https://v.qq.com'
url = 'http://www.baidu.com'
test = 'http://www.httpbin.org'
re = requests.get('http://www.httpbin.org/get')
#print(type(re))
#print(re.status_code)
#print(re.text)
#print(re.cookies)
print(requests.post('http://www.httpbin.org/post'))
print(re.text)

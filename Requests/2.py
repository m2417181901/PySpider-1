import requests
s = requests.session()
s.get('http://httpbin.org/cookies/set/numbie/2016984130509') #模拟登陆
re = s.get('http://httpbin.org/cookies')
print(re.text)

#证书验证
re1 = requests.get('http://www.12306.cn',verify=False) #verify 的意思是证书验证跳过  cert 用与指定证书验证
print(re1.status_code)
from urllib import request,error
try:
    response = request.urlopen('http://cuiqing.com/index.htm')
except error.URLError as e:
    print(e.reason)
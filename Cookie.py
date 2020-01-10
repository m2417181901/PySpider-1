import http.cookiejar,urllib.request,urllib.parse
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#print(response.read())
name = 'cookie.txt'
cook = http.cookiejar.MozillaCookieJar(name)
hander = urllib.request.HTTPCookieProcessor(cook)
opener = urllib.request.build_opener(hander)
response = opener.open('https://v.qq.com')
cook.save(ignore_discard=True,ignore_expires=True)

cook1 = http.cookiejar.MozillaCookieJar()
cook1.load('cookie.txt',ignore_expires=True,ignore_discard=True)
hander1 = urllib.request.HTTPCookieProcessor(cook1)
opener1 = urllib.request.build_opener(hander1)
response1 = opener1.open('https://v.qq.com')
print(response1.read().decode('utf-8'))


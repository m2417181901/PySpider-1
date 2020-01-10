import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
brower = webdriver.Chrome(chrome_options=option)
brower.get('http://urp.hebau.edu.cn:9001')
text = brower.page_source
brower.close()
os.makedirs('./shiwen',exist_ok=True)
s = requests.Session()
url = 'http://urp.hebau.edu.cn:9001'
get_url = 'http://urp.hebau.edu.cn:9001/loginAction.do'

#r = requests.get(url=get_url, headers=headers,cookies=cookie)
#print(r.text)
soup = BeautifulSoup(text, 'lxml')
#a = soup.select('#__VIEWSTATE')[0].attrs.get('value')
#b = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
text_1 = s.get('http://urp.hebau.edu.cn:9001',headers=headers)
print(text_1.text)
image_url = 'http://urp.hebau.edu.cn:9001' + str(soup.select('#vchart')[0].attrs.get('src'))

print(image_url)

# import urllib.request
r = s.get(image_url)
# urllib.request.urlretrieve(image_url, './yanzhengma.jpg')
with open('./shiwen/yanzhengma1.jpg', 'wb') as fp:
    fp.write(r.content)
zh = '2016984130509'
mm = '2016984130509'
v_yzm = input('请输入验证码:')

data = {
    'zjh1':'',
    'tips':'' ,
    'lx':'' ,
    'evalue':'' ,
    'eflag':'',
    'fs':'' ,
    'dzslh':'',
    'zjh':zh,
    'mm':mm,
    'v_yzm':str(v_yzm)
}
r = requests.post(get_url,data=data,headers=headers)
if r:
    print(r.text)














'''''
code = input('请输入验证码:')

post_url = 'http://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE': a,
    '__VIEWSTATEGENERATOR': b,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '17312345678', # 账号
    'pwd': '123456',  # 密码
    'code': code,  # 验证码
    'denglu': '登录',
}

r = s.post(post_url, headers=headers, data=data)

print(r.text)
'''
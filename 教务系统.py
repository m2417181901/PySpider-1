import requests
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://urp.hebau.edu.cn:9005')
print(browser.page_source)
#browser.add_cookie({'JSESSIONID':'ecdx56H28kqyF9XMpVUFw'})
#print(browser.get_cookies())

#data = {'zjh':2016984130509,'mm':2016984130509}
#cookie = {'zjh':2016984130509,'mm':2016984130509}
#r = requests.get('http://urp.hebau.edu.cn:9001',params=cookie)
#ebbrowser.open(r.url)
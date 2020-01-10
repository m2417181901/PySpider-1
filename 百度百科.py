from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import random
start = "https://baike.baidu.com"
his = ["/item/%E5%9F%83%E5%85%8B%E8%8E%B1%E5%B0%94%C2%B7%E6%B3%95%E9%9A%86/7536792?fromtitle=%E9%9B%B7%E9%9C%86&fromid=8883229#viewPageContent"]
for i in range(30):
    url = start+his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    sub_urls = soup.find_all('a',{"target":"_blank","href":re.compile("/item/(%.{2})+$")})
    print(soup.find('title').get_text(),'    url: ', his[-1])
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()




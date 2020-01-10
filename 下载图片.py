import requests
from urllib.request import urlretrieve
import os
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

os.makedirs('./img', exist_ok=True)

# r = urlopen("https://baike.baidu.com/item/%E5%9F%83%E5%85%8B%E8%8E%B1%E5%B0%94%C2%B7%E6%B3%95%E9%9A%86/7536792?fromtitle=%E9%9B%B7%E9%9C%86&fromid=8883229#viewPageContent").read().decode('utf-8')
html = requests.get("http://www.ngchina.com.cn/animals/").text
soup = BeautifulSoup(html, features='lxml')

img = soup.find_all("ul", {"class": "img_list"})
a =1
for img_a in img :
    imgs = img_a.find_all('img')
    for i in imgs:
        r = i['src']
        #   print (r)
        dizhi = "./img/" + str(a) + "f.png"
        a = a + 1
        s = requests.get(r)
        with open(dizhi,'wb') as f:
            for chunk in s.iter_content(chunk_size =128):
                f.write(chunk)
        print('%dimg.png下载成功！' % a)
#
#       urlretrieve(r, dizhi)
#       print('%dimg.png下载成功！' % a)


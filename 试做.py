from bs4 import BeautifulSoup
from urllib .request import urlopen
import requests
import re,os,random,time
os.makedirs('./img/sss3', exist_ok=True)
num = 0
url = ['http://moe.005.tv/76044.html']
a = ['76044.html']
for u in range(30):
    f = BeautifulSoup(urlopen(url[-1]),'lxml')
    tuijian = f.find('div',attrs={'class':'tuijian'})
#    print(tuijian)
    tj = re.findall(r'<a.*?href="(.*?)".*?target="_blank"',str(tuijian),re.S)
    # print(f.text)
    p = f.find('div', attrs={'class': 'fenye'})
    fen = re.findall(r'<a href="(.*?)".*?>', str(p), re.S)
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    if fen:
        for b in fen:
            a.append(b)
            print(b)
    print(f.title)
    for i in a:
        url1 = 'http://moe.005.tv/' + i
        #  print(url1)
        f1 = BeautifulSoup(urlopen(url1), 'lxml')
     #   time.sleep(1.5)
        #  print(f1.find_all('img'))
        n = f1.find_all('img')
        for i in n:
            img = re.findall(r'src="(.*?)"', str(i), re.S)
            for i, c in enumerate(img):
                print(i, c)
                f = './img/sss3/' + str(num) + "号" + '.jpg'
                num += 1
                s = requests.get(c)
                print(type(s))
                with open(f, 'wb') as a:
                    for chunk in s.iter_content(chunk_size=128):  # 下载
                        a.write(chunk)

                    print('下载成功')
    a=[]
    d = []
    for i, c in enumerate(tj):
        url.append(c)
       # d.append(c)
    print(url)
   # url.append(''.join(random.sample(d,1)))

#    print(url[-1])










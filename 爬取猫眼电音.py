import json
import re
import requests
header = 'User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
b=0
for d in range(10):
    url = 'https://maoyan.com/board/4?offset='+str(d*10)
    pa = requests.get(url,header)
    #print(pa.text)
    p = re.compile(r'<dd>.*?title="(.*?)".*?<p.*?class="star".*?>(.*?)</p>.*?</dd>',re.S)
    r = re.findall(p,pa.text)
    print('结束')
    def a(r):
        if r:
            for i in r:
                yield {
                    'title':i[0],
                    'star':i[1]
                }


    with open('title.txt','a',encoding='utf-8') as f:
        for c in a(r):
           b+=1
           f.write(str(b)+json.dumps(c,ensure_ascii=False)+'\n')
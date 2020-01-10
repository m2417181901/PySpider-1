import requests
from time import time
URL = "https://www.bilibili.com/"

def a():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)
        print(r.text)

t1 = time()
a()
print(time()-t1)
a = [[1,2],[3,4]]
b,c = a[0]
print(b,c)
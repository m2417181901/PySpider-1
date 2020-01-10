import requests
import re,os
from bs4 import BeautifulSoup
import json
from urllib.parse import urlencode
from requests.exceptions import RequestException
from hashlib import md5
import time
from urllib.request import urlopen
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
os.makedirs('./今日头条',exist_ok=True)
def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?'+ urlencode(data)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_page_index(html):
    data = json.loads(html)
    #print(data)
   # print(data.keys())
   # print(data.get('city'))
    if data and 'data' in data.keys():
        for item in data.get('data'):
            #print(item)
            yield item.get('article_url')
def get_page_detail(url):
    try:
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
 #   title = re.search(r'<title>(.*?)</title>',soup.text,re.S)
   # print(title.group(1))
    image_pattern = re.compile(r'gallery: JSON.parse\("(.*?)"\)',re.S)
    result = re.search(image_pattern,html)
    if result:
        #data = json.loads(result.group(1).replace('\'', '\"'))
       # print(result.group(1))
        a = result.group(1).replace("\\","")
        urlre = re.findall(r'url":"(.*?)"',a,re.S)
        urlre1 = list(set(urlre))
        urlre1.sort(key=urlre.index)
        if urlre1:
            for i,c in enumerate(urlre1):
                print(i,md5(c.encode()).hexdigest())
                rp =  requests.get(c,headers=headers)
                time.sleep(1)
                save_file(title,rp.content)
                # print (a)
                #  for i  in data.keys:

                #     print(i)
                # if data and 'sub_images' in data.keys:
                #   sub_images = data.get('sub_images')
                #    images = [item.get('url') for item in sub_images]
                #    return images
                #   return {
                #     'title':title,
                #     'url':url,
                #     'images':images
                #   }
def save_file(title,contend):
    path ='今日头条/'+title+md5(contend).hexdigest()+'.jpg'
    if not os.path.exists(path):
        with open(path,'wb') as f:
            for item in contend.iter_content(chunk_size=128):
                f.write(contend)
        print('下载成功')
def main():
    html = get_page_index(0,'街拍')
    #print(html)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            parse_page_detail(html,url)

   # print(html)
if __name__ == '__main__':
    main()




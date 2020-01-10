import requests
import re,os
from bs4 import BeautifulSoup
import eventlet
import time

os.makedirs('G:/Gogend',exist_ok=True)
url = "https://m.dmzj.com/info/38541.html"
head = "https://m.dmzj.com/"
headerss = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

header = {
        'Referer': 'https://manhua.dmzj.com/dogend/',
        'cookle': 'show_tip_1=0; display_mode=0; pt_198bb240=uid=edOEM6GYeqO4gKBq0KblYg&nid=0&vid=JvLvpalHPJIX-RJtcFWA-A&vn=2&pvn=1&sact=1553756426909&to_flag=1&pl=J8gHIAMoYA2Eg1lD2m4zWQ*pt*1553756146653',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

def get_page_index(html):
    response = requests.get(html,headers=headerss,verify=False)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None
def save_file(html,contend,name):
    path =name+'/'+os.path.split(html)[1]
    if not os.path.exists(path):
        with open(path,'wb') as f:
                f.write(contend)
        print('下载成功')
def get_page_detail(text):
    soup = BeautifulSoup(text,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    f = re.findall(r'"id":(.*?),"comic_id":(.*?),"chapter_name":(.*?),',str(soup))
    if f:
        for i in f:
            html = head+'view/'+i[1]+'/'+i[0]+'.html'
            print(html)
            get_image(html,i[2],i[0])
def get_image_index(html,name):
    time.sleep(1)
    print(html)
    for i in html:
        with eventlet.Timeout(15,False):
            reponse = requests.get(i,headers=header,verify=False)
            if reponse.status_code == 200:
                save_file(i,reponse.content,name)
            else:
                print("Error")
    #     print("超时跳过！")
def get_image(html,name,hd):
    f = get_page_index(html)
    path = 'G:/Gogend/'+eval(name)
    os.makedirs(path,exist_ok=True)
    soup = BeautifulSoup(f,'lxml')
    ff = re.findall(r'mReader.initData\((.*?);',str(soup))
    img = re.findall(r'"(https:.*?)"',ff[0])
    imgs = []
    if img:
        for i in range(len(img)):
            img[i] = img[i].replace('\\/', '/')
            imgs.append(eval(repr(img[i]).replace('\\\\', '\\')))
    print(imgs)
    get_image_index(imgs,path)


if __name__ == '__main__':
    ff = get_page_index(url)
    get_page_detail(ff)


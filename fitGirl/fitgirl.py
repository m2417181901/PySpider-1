import requests
from urllib3 import response
import re
from bs4 import BeautifulSoup
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
headers = {
'Cookie':'SUV=00444052DDC3330A5C04E9E5A671D660; CXID=B8EB71DFED88F47B95DE19D7D0761793; SUID=0A33C3DD5D68860A5C06459A00097E9E; sw_uuid=4444876063; ssuid=2648530108; ad=yyllllllll2ty$cmlllllVejrAclllllWEyL$kllll9lllll9Zlll5@@@@@@@@@@; IPLOC=CN1305; ABTEST=0|1548328690|v1; weixinIndexVisited=1; sct=2; SNUID=965EDD13686CE84A6ECDA20A696266C7; ppinf=5|1549358085|1550567685|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklODAlODYlRTUlODUlODl8Y3J0OjEwOjE1NDkzNTgwODV8cmVmbmljazoxODolRTklODAlODYlRTUlODUlODl8dXNlcmlkOjQ0Om85dDJsdUplcG5RUnhNSWhJUUhFUUM0dDExTlVAd2VpeGluLnNvaHUuY29tfA; pprdig=kszHiiy4D5Enui7eiidaYwKJDKwj1sLs-kpl2T0kOjECJyj-m1s8mkk6Ckvyzi90KkFFjN10HYQJzWtJKLxFP2ttxZVJZbGzDmv2uXPlGtl_cOlaWbpi7NpgULDt-uwYkJH-44eo-4rnW68YHR_wBvw8eeXtOdO6lpKgqiJ9GFo; sgid=09-39161169-AVxZVAXcaKiaC7p8rF12VPkw',
'Host':'weixin.sogou.com',
'Referer':'https://open.weixin.qq.com/connect/qrconnect?appid=wx6634d697e8cc0a29&scope=snsapi_login&response_type=code&redirect_uri=https%3A%2F%2Faccount.sogou.com%2Fconnect%2Fcallback%2Fweixin&state=72437257-f610-40eb-a630-dacc93dfe1e0&href=https%3A%2F%2Fdlweb.sogoucdn.com%2Fweixin%2Fcss%2Fweixin_join.min.css%3Fv%3D20170315&lang=zh_CN',
'Upgrade-Insecure-Requests':1,
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

url2 = 'http://www.dilidili.wang/anime/sao/'
url = 'http://fitgirl-repacks.site'
def get_html(url):
    reponst = requests.get(url,headers=headers)

    if reponst.status_code == 200:
        reponst.encoding = reponst.apparent_encoding
        return reponst.text

    else:
        print('状态码错误')
def parse_html_index(html):
    reponst = get_html(html)
    soup = BeautifulSoup(reponst,'lxml')
    return soup.select('img')



ff = parse_html_index(url2)
print(ff)


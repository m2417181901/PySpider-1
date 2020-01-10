from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
res = re.findall(r"<title>(.*?)</title>",html,flags=re.DOTALL)
html2 = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
soup = BeautifulSoup(html2,features='lxml')
all_href = soup.find_all('a')
img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
http_links = soup.find_all('a',{'href':re.compile('https://morvan.*')})
for link in http_links:
    print(link.get_text())



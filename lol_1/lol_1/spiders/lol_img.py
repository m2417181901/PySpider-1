# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from lol_1.items import Lol1Item
class LolImgSpider(scrapy.Spider):
    name = 'lol_img'
    allowed_domains = ['http://www.hentaipornpics.net/tags/stockings/3']
    start_urls = ['http://www.hentaipornpics.net/tags/stockings/3/']
    base_domin = 'http://www.hentaipornpics.net'
    def start_requests(self):
        return [Request(url='http://www.hentaipornpics.net/tags/stockings/3', meta={'cookiejar': 1}, callback=self.find_url)]
    def find_url(self,response):
        url = response.xpath("//div[@class='portfolio-post']")
        for i in url:
            url2 = re.search(r'href="(.*?)"',str(i.get()))
         #   print(i.get())
         #   print(url2.group(1))
            yield Request(url=self.base_domin+url2.group(1),meta={'cookiejar': 1},callback=self.parse,dont_filter=True)

    def parse(self, response):
        url = response.xpath("//figure[@class='box']")
        title = response.xpath("//h1[@class='page-title']/text()").get()
        for i in url:
            item = Lol1Item()
            url2 = re.search(r'data-img="(.*?)"',str(i.get()))
            image = url2.group(1)+".jpg"
            item['image_urls'] = [image]
            item['category'] = title
            yield item
        for i in range(4,10):
            url3 = "http://www.hentaipornpics.net/tags/stockings/" + str(i)
            yield Request(url=url3,meta={'cookiejar': 1},callback=self.find_url,dont_filter=True)


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from lol_1.settings import IMAGES_STORE
import os
class Lol1Pipeline(object):
    def process_item(self, item, spider):
        return item

class Lol1ImagesPipeline(ImagesPipeline):
    #这个方法在发送下载请求之前调用
    #其实这个方法本身就是去发送下载请求的
    def get_media_requests(self, item, info):
        request_objs = super(Lol1ImagesPipeline,self).get_media_requests(item,info)
        for requess_obj in request_objs:
            requess_obj.item = item
        return request_objs


    def file_path(self, request, response=None, info=None):
        path = super(Lol1ImagesPipeline, self).file_path(request,response,info)
        category = request.item.get('category')
        image_store = IMAGES_STORE
        category_path = os.path.join(image_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_mame = path.replace("full/","")
        image_path = os.path.join(category_path,image_mame)
        return image_path

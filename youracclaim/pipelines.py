# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import cloudant

class YouracclaimPipeline(object):
    
    def __init__(self):
        # 可选实现，做参数初始化等
        
    def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        self.serviceUsername = "f5e06e7f-c8b6-4d4a-b25b-560c7da7c363-bluemix"
        self.servicePassword = "368e4fca14c81c076edf9ace095eafa51945059e13c37ed46a847af4aad9cfe4"
        self.serviceURL = "f5e06e7f-c8b6-4d4a-b25b-560c7da7c363-bluemix.cloudant.com"
        self.client = cloudant(serviceUsername, servicePassword, url=serviceURL)
        #account = cloudant.Account('elevenlibrary', async=True)
        database = account.database('elevenlibrary')
    
        print("result->" + database.get().result().json())
        
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
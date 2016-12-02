# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class XunyeeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
from scrapy.item import Item, Field

class XYmoiveItem(Item):
    name=Field()#电视名
    amount=Field()#播放量
    place=Field()#排名
    # director=Field()#导演
    # classification=Field()#分类
    # actor=Field()#演员
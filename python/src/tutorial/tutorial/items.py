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


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class XiaoHuarItem(scrapy.Item):
    name = scrapy.Field()
    school = scrapy.Field()
    urlprefix = scrapy.Field()
    imgurl = scrapy.Field()


class SexyBeautyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


class MmjpgItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

import scrapy
from scrapy.loader import ItemLoader

from tutorial.items import MmjpgItem


class MmjpgSpider(scrapy.Spider):
    name = 'mmjpg'
    allowed_domains = ["mmjpg.com"]
    start_urls = ['http://www.mmjpg.com/']

    def parse(self, response):
        for href in response.css('div.pic li').css('a::attr(href)'):
            yield response.follow(href, callback=self.myparse)

        next_page = response.css('div.page').css('a.ch ::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def myparse(self, response):
        l = ItemLoader(item=MmjpgItem(), response=response)
        l.add_value('name', response.css('div.article h2::text').extract_first())
        l.add_value('url', response.css('div.content img').xpath('@src').extract_first())
        yield l.load_item()
        next_page = response.css('div.page').css('a.next ::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.myparse)

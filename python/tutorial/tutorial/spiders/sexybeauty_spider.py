import scrapy
from scrapy.loader import ItemLoader

from tutorial.items import SexyBeautyItem


class SexyBeautySpider(scrapy.Spider):
    name = 'sexyBeauty'
    allowed_domains = ["mm131.com"]
    start_urls = ['http://www.mm131.com/xinggan/']

    def parse(self, response):
        for href in response.css('dl.list-left').css('dd a::attr(href)'):
            if href.extract().find('list') != -1:
                continue
            yield response.follow(href, callback=self.myparse)

        next_page = response.css('dd.page').xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        if next_page is not None:
            url = 'http://www.mm131.com/xinggan/' + next_page
            yield response.follow(url, callback=self.parse)

    def myparse(self, response):
        l = ItemLoader(item=SexyBeautyItem(), response=response)
        l.add_value('name', response.css('div.content h5::text').extract_first())
        l.add_value('url', response.css('div.content-pic img').xpath('@src').extract_first())
        yield l.load_item()
        next_page = response.css('div.content-page').xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.myparse)

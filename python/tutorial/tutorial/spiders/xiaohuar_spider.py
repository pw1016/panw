import scrapy
from scrapy.loader import ItemLoader

from tutorial.items import XiaoHuarItem


class XiaoHuarSpider(scrapy.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = ["http://www.xiaohuar.com/hua/"]

    def parse(self, response):
        for div in response.css('div.img'):
            l = ItemLoader(item=XiaoHuarItem(), response=response)
            l.add_value('name', div.css('span.price::text').extract())
            l.add_value('school', div.css('div.btns a::text').extract())
            l.add_value('urlprefix', div.css('div.btns a::attr(href)').extract())
            l.add_value('imgurl', div.css('img').xpath('@src').extract())
            yield l.load_item()

        next_page = response.css('div.page_num').xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        print('next_page: ' + next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

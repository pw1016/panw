import scrapy
from scrapy.loader import ItemLoader

from tutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # yield {
            #     'text': quote.css('span.text::text').extract_first(),
            #     'author': quote.css('small.author::text').extract_first(),
            #     'tags': quote.css('div.tags a.tag::text').extract()
            # }

            # next_page = response.css('li.next a::attr(href)').extract_first()
            # if next_page is not None:
            #     # next_page = response.urljoin(next_page)
            #     # yield scrapy.Request(next_page, callback=self.parse)
            #     yield response.follow(next_page, callback=self.parse())

            l = ItemLoader(item=QuotesItem(), response=response)
            l.add_value('text', quote.css('span.text::text').extract_first())
            l.add_value('author', quote.css('small.author::text').extract_first())
            l.add_value('tags', quote.css('div.tags a.tag::text').extract())
            yield l.load_item()

            for a in response.css('li.next a'):
                yield response.follow(a, callback=self.parse)

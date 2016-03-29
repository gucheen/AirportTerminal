from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from AirportTerminal.items import AirportTermianlItem
from scrapy.http import Request


class V2EXSpider(BaseSpider):
    name = "V2EX"
    allow_domains=["v2ex.com"]
    start_urls = ["http://www.v2ex.com"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//h1/text()').extract()
        for title in titles:
            item = AirportTermianlItem()
            item["title"] = title
            yield item

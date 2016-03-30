import scrapy


class V2EXSpider(scrapy.Spider):
    name = "V2EX"
    allow_domains = ["v2ex.com"]
    start_urls = ["http://www.v2ex.com"]
    DOWNLOAD_DELAY = 3

    def parse(self, response):
        for href in response.css('#Main span.item_title > a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_topic)

    def parse_topic(self, response):
        yield {
            'title': response.css('#Main > div:nth-child(2) > div.header > h1::text').extract()[0],
            'author': response.css('#Main > div:nth-child(2) > div.header > small > a::text').extract()[0],
            'content': response.css('#Main > div:nth-child(2) > div.cell > div::text').extract(),
            'link': response.url
        }

# -*- coding: utf-8 -*-
import scrapy
import scrapy.loader
from AirportTerminal.items import BangumiTvItem

BASIC_URL = 'http://bgm.tv/game/tag/galgame/?sort=rank&page=%d'
START_PAGE = 1
NUMBER_OF_PAGE = 100


class BangumiTvSpider(scrapy.Spider):
    name = "bangumi_tv"
    allowed_domains = ["bgm.tv"]
    start_urls = (
        BASIC_URL % 1,
    )

    def __init__(self):
        self.page_number = START_PAGE

    def start_requests(self):
        for i in range(self.page_number, self.page_number + NUMBER_OF_PAGE):
            yield scrapy.Request(url=BASIC_URL % i, callback=self.parse_rank_page)

    def parse_rank_page(self, response):
        for item in response.xpath('//*[@class="item odd clearit"]'):
            subject_link = response.urljoin(item.xpath('a/@href').extract_first())
            yield scrapy.Request(subject_link, callback=self.parse_subject_page)

    def parse_subject_page(self, response):
        item = scrapy.loader.ItemLoader(item=BangumiTvItem(), response=response)
        item.add_xpath('original_title', '//*[@id="headerSubject"]/h1/a/text()')
        item.add_value('link', response.url)
        item.add_css('score', '.global_score .number::text')
        item.add_css('bangumi_rank', '.global_score .alarm::text', re='#(\d+)')
        yield item.load_item()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class V2EXItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()


class BangumiTvItem(scrapy.Item):
    original_title = scrapy.Field()
    link = scrapy.Field()
    score = scrapy.Field()
    bangumi_rank = scrapy.Field()

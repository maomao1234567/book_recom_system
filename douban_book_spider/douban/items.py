# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    """定义爬取图书信息的item"""

    book_name = scrapy.Field()
    author = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()

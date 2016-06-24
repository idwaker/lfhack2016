# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    industry = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    openings = scrapy.Field()
    level = scrapy.Field()
    posted_date = scrapy.Field()

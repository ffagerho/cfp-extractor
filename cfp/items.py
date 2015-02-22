# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CfpItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()
    when = scrapy.Field()
    where = scrapy.Field()
    submission_deadline = scrapy.Field()
    notification_due = scrapy.Field()
    final_version_due = scrapy.Field()
    text = scrapy.Field()

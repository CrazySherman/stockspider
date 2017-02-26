# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StatsDate(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # the latest financial release date of the stock
   	date = scrapy.Field()
   	# inc name
   	inc = scrapy.Field()
    

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from stockspider.file_utils import incs, write_back


class StockspiderPipeline(object):
    def process_item(self, item, spider):
    	print '[Debugging]:: item received ', item
        if item["inc"] not in incs or incs[item["inc"]] != item["date"]:
        	print "[Debugging]:: item needs update"
        	incs[item["inc"]] = item["date"]
        	write_back(incs)
        return item

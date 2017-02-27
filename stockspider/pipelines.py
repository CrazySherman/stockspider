# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from stockspider.file_utils import load_current_incs, write_back
from sendemail.mymail import sendout_email

class StockspiderPipeline(object):
    incs = load_current_incs()
    needupdate = False
    def process_item(self, item, spider):
    	print '[Debugging]:: item received ', item
        incs = StockspiderPipeline.incs    # reference the static variable
        if item["inc"] not in incs or incs[item["inc"]] != item["date"]:
        	print "[Debugging]:: item needs update"
        	incs[item["inc"]] = item["date"]
        	StockspiderPipeline.needupdate = True
            # send out email becareful when you test this part
            # sendout_email(item["inc"])

        return item
    def close_spider(self, spider):
        if StockspiderPipeline.needupdate:
            write_back(StockspiderPipeline.incs)
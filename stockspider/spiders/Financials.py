import scrapy
from stockspider.items import StatsDate
# this shit should only read from the file module
from stockspider.file_utils import load_current_incs
import re


class Financials(scrapy.Spider):
	# caveat: start_urls will override the start_request method
	my_start_urls = ["https://www.google.com/finance?q=NASDAQ%3AAMZN&fstype=ii"]   # sample url format
	template = ("https://www.google.com/finance?q=NASDAQ%3A", "&fstype=ii")
	name = "Financials"
	def __init__(self):
		print "[Debugging]:: spider started"

	def start_requests(self):

		print "[Debugging]:: start requesting..."
		# format urls
		del self.my_start_urls[:]
		incs = load_current_incs()
		for name, date in incs.items():
			url = self.template[0] + name + self.template[1]
			print "[Debugging]:: requesting ", url
			self.my_start_urls.append(url)
			yield scrapy.Request(url, self.parse, meta = {'inc': name})

	def parse(self, response):
		cols = response.xpath('/html//div[@id="incinterimdiv"]//th/text()')
		latest = ''
		p = re.compile('[0-9]+\-[0-9]+\-[0-9]+')
		for col in cols:
			statement = col.extract()
			if "ending" in statement:
				# this is a date statement
				m = p.search(statement)
				if not m:
					print '[Error]: cannot parse the date, website formate might changed'
					break
				else:
					date = m.group()
					latest = date if date > latest else latest
		item = StatsDate()
		print '[Debugging]:: latest date parsed is ', latest
		item["date"] = latest
		item["inc"] =response.meta['inc']
		return item

			
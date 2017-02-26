using file IO is stupid
we should really use database, but should we?


## basic usage
scrapy crawl -L INFO Financials > application.log


## todos
* peel off the trailing carriage return of incs list file, or anything else other than alphabetic chars
* use static variable (class variable) for incs dict to avoid concurrency issues for frequently calling write_back
* add smtp client

# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jobcrawler.spiders.merojob_spider import MeroJobSpider
from jobcrawler.spiders.ramrojob_spider import RamroJobSpider



if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(MeroJobSpider)
    process.crawl(RamroJobSpider)
    process.start()

# -*- coding: utf-8 -*-

import re
import urllib
import scrapy
from ..items import JobCrawlerItem


class RamroJobSpider(scrapy.Spider):
    """
    Spider for merojob site
    """
    name = 'ramrojob'
    allowed_domains = ['ramrojob.com']
    start_urls = [
        'http://www.ramrojob.com/industry/jobs-by-industry/0/page/0'              
    ]
#    search_url = 'http://www.merojob.com/search-new/?category={}&orgtype={}&location=0&ajax=true'
    
    def parse(self, response):
        # find all industry listing
        industries = response.css('div.list-unstyled a')
        for each in industries:
            metadata = {
                'industry': each.xpath('text()').extract()[0].strip()            
            }
            yield scrapy.Request(each.xpath('@href').extract()[0],
                                 self.parse_listings, meta=metadata)

    def parse_listings(self, response):
        items = response.css("h4.pos-title a::attr('href')")
        for link in items.extract():
            yield scrapy.Request(link, self.parse_item, meta=response.meta)
        
        # get next page
        next_pagination = response.xpath('//ul[contains(@class, "pagination")]/li[contains(@class, "active")]/following-sibling::li[1]/a/@href')
        if next_pagination:
            yield scrapy.Request(next_pagination.extract()[0],
                                 self.parse_listings, meta=response.meta)

    def parse_item(self, response):
        item = JobCrawlerItem()
#        item['category'] = response.meta['category']
        item['industry'] = response.meta['industry']

        # general section
        content_div = response.css('div.jobs-detail-inner')
        if content_div:
            title = response.css('h1.red-title::text').extract()[0]
            title = re.sub(r'\s+', ' ', title)
            item['title'] = title.strip().strip('Job Position :')
            
            # Job Location: Kathmandu
            location_xpath = '//table/tr/td[contains(text(), "Job Location")]/following-sibling::td[2]/text()'
            location = content_div.xpath(location_xpath)
            item['location'] = location.extract()[0] if location else ''
    
            # No. of Vacancies :
            vacancy_xpath = '//table/tr/td[contains(text(), "No. of Vacancies")]/following-sibling::td[2]/text()'
            vacancies = content_div.xpath(vacancy_xpath)
            item['openings'] = vacancies.extract()[0] if vacancies else 1
    
            # Posted Date :
            posted_date_xpath = '//table/tr/td[contains(text(), "Posted Date")]/following-sibling::td[2]/text()'
            posted_date = content_div.xpath(posted_date_xpath)
            item['posted_date']= posted_date.extract()[0] if posted_date else ''
    
            # Job Level :
            level_xpath = '//table/tr/td[contains(text(), "Job Level")]/following-sibling::td[2]/text()'
            level = content_div.xpath(level_xpath)
            item['level'] = level.extract()[0] if level else ''
            
            cat_xpath = '//table/tr/td[contains(text(), "Job Category")]/following-sibling::td[2]/text()'
            cat = content_div.xpath(cat_xpath)
            item['category'] = cat.extract()[0] if cat else ''

        
        yield item


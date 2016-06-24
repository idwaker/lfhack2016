# -*- coding: utf-8 -*-

import urllib
import scrapy
from ..items import JobCrawlerItem


class MeroJobSpider(scrapy.Spider):
    """
    Spider for merojob site
    """
    name = 'merojob'
    allowed_domains = ['merojob.com']
    start_urls = [
        'http://www.merojob.com/search-new/'              
    ]
    search_url = 'http://www.merojob.com/search-new/?category={}&orgtype={}&location=0&ajax=true'
    
    def parse(self, response):
        # find all category listing and industry listing
        category_select = response.css('select#category')
        industry_select = response.css('select#orgtype')
        
        # space_to_plus = lambda x: x.strip().replace('%2B', '+')
        
        for category in category_select.css("option::attr('value')").extract():
            if category == '0':
                continue
            for industry in industry_select.css("option::attr('value')").extract():
                if industry == '0':
                    continue
                metadata = {
                    'category': category,
                    'industry': industry
                }
                yield scrapy.Request(self.search_url.format(urllib.quote(category, safe=''),
                                                            urllib.quote(industry, safe='')),
                                     self.parse_listing, meta=metadata)
#        category_div = response.css('div.dividetwo')
#        interested = [item for item in category_div.css('li')
#                      if 'IT' in item.extract()]
#        for each in interested:
#            # print(each.xpath('a/@href').extract())
#            yield scrapy.Request(each.xpath('a/@href').extract()[0],
#                                 self.parse_category)

    def parse_listing(self, response):
        for link in response.css("a.spacebot::attr('href')").extract():
            yield scrapy.Request(link, self.parse_item, meta=response.meta)

    def parse_item(self, response):
        item = JobCrawlerItem()
        item['category'] = response.meta['category']
        item['industry'] = response.meta['industry']

        # general section
        content_div = response.css('div#content_newa')
        if content_div:
            item['title'] = content_div.css('h1.h::text').extract()[0]
            
            # Job Location: Kathmandu
            location_xpath = '//dt[contains(text(), "Job Location :")]/following-sibling::dd[1]/text()'
            location = content_div.xpath(location_xpath)
            item['location'] = location.extract()[0] if location else ''
    
            # No. of Vacancies :
            vacancy_xpath = '//dt[contains(text(), "No. of Vacancies :")]/following-sibling::dd[1]/text()'
            vacancies = content_div.xpath(vacancy_xpath)
            item['openings'] = vacancies.extract()[0] if vacancies else 1
    
            # Posted Date :
            posted_date_xpath = '//dt[contains(text(), "Posted Date :")]/following-sibling::dd[1]/text()'
            posted_date = content_div.xpath(posted_date_xpath)
            item['posted_date']= posted_date.extract()[0] if posted_date else ''
    
            # Job Level :
            level_xpath = '//dt[contains(text(), "Job Level :")]/following-sibling::dd[1]/text()'
            level = content_div.xpath(level_xpath)
            item['level'] = level.extract()[0] if level else ''
        else:
            # company pages
            content_div = response.css('div.content')
            subblocks = content_div.css('div.subblock')
            if subblocks:
                for div in subblocks:
                    _item = item.copy()
                    _item['title'] = div.css('h1.h1 strong::text').extract()[0]

                    # Job Location
                    location = div.xpath('//p[contains(text(), "Job Location :")]/text()')
                    _item['location'] = location.extract()[0].strip().strip('Job Location :') if location else ''
    
                    # No. of Vacancy: 1
                    vacancies = div.xpath('//p[contains(text(), "No. of Vacancy:")]/text()')
                    _item['openings'] = vacancies.extract()[0].strip().strip('No. of Vacancy:') if vacancies else 1

                    _item['posted_date'] = ''
                    _item['level'] = ''
                    yield _item
            else:
                title = content_div.css('h1.h1 strong::text')
                if title:
                    item['title'] = title.extract()[0]
                else:
                    item['title'] = content_div.css('h2.heading strong::text').extract()[0]

                # Job Location
                location = content_div.xpath('//p[contains(text(), "Job Location :")]/text()')
                item['location'] = location.extract()[0].strip().strip('Job Location :') if location else ''

                # No. of Vacancy: 1
                vacancies = content_div.xpath('//p[contains(text(), "No. of Vacancy:")]/text()')
                item['openings'] = vacancies.extract()[0].strip().strip('No. of Vacancy:') if vacancies else 1

                item['posted_date'] = ''
                item['level'] = ''
                yield item
        
        yield item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from datetime import date, datetime
from scrapy.exceptions import DropItem
from .mappings import DISTRICTS, INDUSTRY_FILTERS, CATEGORY_FILTERS


class CleanDataPipeline(object):
    
    def process_item(self, item, spider):
        item['title'] = item['title'].strip()
        try:
            item['openings'] = int(item['openings'])
        except ValueError:
            item['openings'] = 1
        return item


class NormalizeDatePipeline(object):
    
    def process_item(self, item, spider):
        if item['posted_date']:
            for format_string in ['%B %d, %Y',]:
                try:
                    posted_date = datetime.strptime(item['posted_date'], format_string)
                except ValueError:
                    continue
                else:
                    item['posted_date'] = posted_date.strftime('%Y-%m-%d')
                    break
        return item


class NormalizeDistrictPipeline(object):
    
    def process_item(self, item, spider):
        if item['location']:
            location = item['location'].lower()
            for dis in DISTRICTS:
                if dis in location:
                    item['location'] = dis.capitalize()
        return item

        
class FilterIndustryPipeline(object):
    
    def process_item(self, item, spider):
        industries = INDUSTRY_FILTERS[spider.name]
        if industries:
            if item['industry']:
                _found = False
                for industry, listings in industries.items():
                    if item['industry'].strip().lower() in (x.lower() for x in listings):
                        item['industry'] = industry
                        _found = True
                if not _found:
                    raise DropItem("Dropping...")
            else:
                raise DropItem("dropping...")
        return item


class FilterCategoryPipeline(object):
    
    def process_item(self, item, spider):
        categories = CATEGORY_FILTERS[spider.name]
        if categories:
            if item['category']:
                _found = False
                for category, listings in categories.items():
                    if item['category'].strip().lower() in (x.lower() for x in listings):
                        item['category'] = category
                        _found = True
                if not _found:
                    raise DropItem("Dropping...")
            else:
                raise DropItem("dropping...")
        return item

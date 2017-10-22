# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # job
    Job_name = scrapy.Field()
    Job_location = scrapy.Field()
    Job_salary = scrapy.Field()
    Job_update = scrapy.Field()  # i4
    Job_url = scrapy.Field()  # response.url

    # requirment
    Require_exp = scrapy.Field()  # i1
    Require_degree = scrapy.Field()  # i2
    Require_number = scrapy.Field()  # i3
    Require_lan = scrapy.Field()  # i5

    # company
    Company_name = scrapy.Field()
    Company_type = scrapy.Field()
    Company_scale = scrapy.Field()
    Company_field = scrapy.Field()

    Location = scrapy.Field()

    pass

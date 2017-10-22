# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from job51.items import Job51Item



class HzJobSpider(CrawlSpider):
    name = 'hz_job'
    allowed_domains = ['search.51job.com','jobs.51job.com']
    start_urls = ['http://search.51job.com/list/080200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    rules = (
        Rule(LinkExtractor(restrict_css='li.bk>a')),
        Rule(LinkExtractor(restrict_css='p.t1 a'),callback='parse_item')
    )

    def parse_item(self, response):
        l = ItemLoader(item=Job51Item(),response=response)
        l.add_value('Job_url',response.url)
        l.add_xpath('Job_name',xpath='//div[@class="cn"]/h1/@title')
        l.add_xpath('Job_location','//span[@class="lname"]/text()')
        l.add_xpath('Job_salary','//div[@class="cn"]/strong/text()')
        l.add_xpath('Company_name','//p[@class="cname"]/a/@title')
        l.add_xpath('Company_type','//p[@class="msg ltype"]/text()')#item pipeline[0]
        l.add_xpath('Require_exp','//div[@class="jtag inbox"]//span[@class="sp4"]/text()')#pipeline
        l.add_xpath('Location','//p[@class="fp"]/text()')

        return l.load_item()
'''
    #requirment
    Require_exp=scrapy.Field()#i1
    Require_dgree=scrapy.Field()#i2
    Require_number=scrapy.Field()#i3
    Require_lan=scrapy.Field()#i5
    Require_major=scrapy.Field()#i6
'''
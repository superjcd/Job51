# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class CompanyPipeline(object):
    def process_item(self, item, spider):
        if item['Company_type']:
            replace = re.findall(pattern='\W(\w+)\W', string=item['Company_type'][0])
            item['Company_type'] = replace[0]
            item['Company_scale'] = replace[1]
            item['Company_field'] = replace[2:]

        if item['Require_exp']:
            target_list=item['Require_exp']
            for i in target_list:
                if re.search(pattern="经验", string=i):
                    item['Require_exp'] = i

                if re.search(pattern='高中|中专|大专|本科|硕士|博士', string=i):
                    item['Require_degree'] = i

                if re.search(pattern='人', string=i):
                    item['Require_number'] = i

                if re.search(pattern='发布', string=i):
                    item['Job_update'] = i

                if re.search(pattern='语|话', string=i):
                    item['Require_lan'] = i

        if item['Location']:
            targets=item['Location']
            for i in targets:
                if re.search(pattern='(\w+)\W+', string=i):
                    item['Location']=i

        return item

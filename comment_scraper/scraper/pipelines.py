# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):
    def process_item(self, item, spider):
    	if item['datetime']:
    		item['datetime'] = '2017-' + item['datetime']			# add customize 'datatime'
    	if spider.conf['DO_ACTION']: #Necessary since DDS v.0.9+
            try:
                item['news_website'] = spider.ref_object

                # checker_rt = SchedulerRuntime(runtime_type='C')	# save infomation of Scheduler runtimes
                # checker_rt.save()
                # item['checker_runtime'] = checker_rt

                item.save()
                spider.action_successful = True
                spider.log("Item saved.", logging.INFO)

            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
      	else:
          	if not item.is_valid():
				spider.log(str(item._errors), logging.ERROR)
              	raise DropItem("Missing attribute.")
        return item

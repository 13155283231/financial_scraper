# -*- coding: utf-8 -*-

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "financial_scraper.settings") #Changed in DDS v.0.3

BOT_NAME = 'comment_scraper'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'comment_scraper.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')


EXTENSIONS = {
    'comment_scraper.scraper.extensions.totaltime.ExtensionThatAccessStats': 524,
}		

#Scrapy 0.20+
ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'comment_scraper.scraper.pipelines.DjangoWriterPipeline': 800,
}

# in order to Remove duplicates
# DUPEFILTER_CLASS = 'comment_scraper.scraper.duplicate_filter.CustomFilter'

# CONCURRENT_REQUESTS=32

CONCURRENT_ITEMS=200					# big num, this can improve speed of scrape #defaut=100

# LOG_FILE='lately_log.txt'

# LOG_LEVEL='INFO'

DOWNLOAD_TIMEOUT = 10
import logging
from scrapy import signals

logger = logging.getLogger(__name__)

class ExtensionThatAccessStats(object):

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
    	exp = cls(crawler.stats)					# must to be Instantiation
    	crawler.signals.connect(exp.close_spider, signal=signals.engine_stopped)
        return exp

    def close_spider(self):
    	logger.info(self.stats.get_value('finish_time')-self.stats.get_value('start_time'))
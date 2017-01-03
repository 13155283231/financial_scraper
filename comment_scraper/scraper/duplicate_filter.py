#-*-coding:utf-8 -*-
import os
import logging
from scrapy.dupefilters import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

class CustomFilter(RFPDupeFilter):
    def __getid(self, url):
        # mm = url.split("&refer")[0] #or something like that
        mm = url
        return mm

    def request_seen(self, request):
        fp = self.__getid(request.url)
        if fp in self.fingerprints:
            return True
        logger = logging.getLogger()
        logger.info("-->add")
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)

# scrapy自带的去重 貌似没什么用
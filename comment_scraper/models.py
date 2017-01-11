from __future__ import unicode_literals

from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem

# Create your models here.
class NewsWebsite(models.Model):                        # The name of the site to be crawled
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

# sentiment analysis result
class Analysis(models.Model):
    stock_code = models.IntegerField(default=None)
    stock_name = models.CharField(max_length=20)
    pos_degree = models.FloatField(default=None)
    key = models.CharField(max_length=100)


class Comment(models.Model):
    news_website = models.ForeignKey(NewsWebsite)
    stock_code = models.IntegerField(default=None)
    stock_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    url   = models.URLField(default='http://')
    username = models.CharField(max_length=20)
    user_url = models.URLField()
    datetime = models.DateTimeField(null=True, blank=True)
    # May be used to determine whether there is exists, improve efficiency.
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

class CommentItem(DjangoItem):
    django_model = Comment
    # You can store the item class (here: ArticleItem) telling Scrapy 
    # which model class to use for storing the data directly underneath 
    # the associated model class.

@receiver(pre_delete)                       # Easy to delete
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, NewsWebsite):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()
    
    if isinstance(instance, Comment):
        if instance.checker_runtime:
            instance.checker_runtime.delete()
            
pre_delete.connect(pre_delete_handler)
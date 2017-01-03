from dynamic_scraper.spiders.django_spider import DjangoSpider
from comment_scraper.models import NewsWebsite, Comment, CommentItem


class CommentSpider(DjangoSpider):

    name = 'comment_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(NewsWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Comment
        self.scraped_obj_item_class = CommentItem
        super(CommentSpider, self).__init__(self, *args, **kwargs)
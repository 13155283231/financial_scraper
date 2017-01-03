from django.contrib import admin
from comment_scraper.models import NewsWebsite, Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('stock_code','stock_name', 'title','datetime')
    list_display_links = ('title',)
   

admin.site.register(NewsWebsite)
admin.site.register(Comment,CommentAdmin)

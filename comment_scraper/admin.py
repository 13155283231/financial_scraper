from django.contrib import admin
from comment_scraper.models import NewsWebsite, Comment,Analysis
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('stock_code','stock_name', 'title','datetime')
    list_display_links = ('title',)
   
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('stock_code','stock_name', 'pos_degree')
    list_display_links = ('stock_name',)

admin.site.register(NewsWebsite)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Analysis,AnalysisAdmin)
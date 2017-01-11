# coding:utf-8
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from comment_scraper.sentiment_analy import start_analysis as sa
from .models import Comment

# Create your views here.
def index(request):
	template = loader.get_template('comment_scraper/index.html')
	comment_list = Comment.objects.order_by('stock_code')[:5]
	context = {
        'comment_list': comment_list,
    }
	return HttpResponse(template.render(context))

# 计算出积极度，保存到数据库
def get_pos(request, stock_id):
	v = sa.save_to_db(int(stock_id))
	return HttpResponse(v)

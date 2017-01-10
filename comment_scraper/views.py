from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from comment_scraper.sentiment_analy import start_analysis as sa
import datetime
# Create your views here.
def index(request):
	now = datetime.datetime.now()
	template = loader.get_template('comment_scraper/index.html')
	context = {"str":"hello",'current_date': now}
	return HttpResponse(template.render(context))

def get_pos(request, stock_id):
	v = sa.pos_value(int(stock_id))
	return HttpResponse(v)

from django.shortcuts import render
from django.http import HttpResponse
from comment_scraper.sentiment_analy import start_analysis as sa
# Create your views here.
def index(request):
	# v = sa.pos_value(id)
	return HttpResponse("Hello word!!")

def get_pos(request, stock_id):
	v = sa.pos_value(int(stock_id))
	return HttpResponse(v)
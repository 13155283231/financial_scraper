from django.conf.urls import url

from . import views

# this set can match diffrently app.
urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^(?P<stock_id>[0-9]{6})/pos$', views.get_pos, name='get_pos'),		# positive api
]
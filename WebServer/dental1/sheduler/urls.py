from django.conf.urls import url

from . import views


app_name = 'sheduler'
urlpatterns = [
	url(r'^$', views.index_order, name='index_order'),
	url(r'^new/order/$', views.add, name='add'),
]
from django.conf.urls import url

from . import views

app_name = 'carsales_calc'
urlpatterns = [
	# ex: /carsales_calc/
#     url(r'^$', views.index, name='index'),
    # ex: /carsales_calc/search/
    url(r'^search/$', views.search, name="search"),
    # ex: /search/5/results/
    url(r'^results/(?P<pk>[\d\.]+)$', views.results, name="results"),
    # ex: /search/5/averages/
    # url(r'^(?P<search_id>[0-9]+)/averages/$', views.averages, name='averages')
]
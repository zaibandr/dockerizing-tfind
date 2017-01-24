from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^search/$', views.torrent_search_form, name='search_form'),
    url(r'^autocomplete/$', views.autocomplete, name='autocomplete'),
    url(r'^torrents/(?P<trend>.*)', views.url_parse_search, name='torrent')
]
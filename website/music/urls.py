'''
Created on Oct 15, 2016

@author: Pavan
'''
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),
    #/music/id example: /music/1
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favourite, name='favourite'),
]
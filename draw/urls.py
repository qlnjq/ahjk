# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#     url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('allVersions/', views.allVersions, name='allVersions'),
    path('compare/', views.compare, name='compare'),
]


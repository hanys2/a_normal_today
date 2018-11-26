#blog
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^index', views.index, name='index'),
    #url(r'^2', views.post_list2, name='post_list2'),
    #url(r'^3', views.post_list3, name='post_list3'),
    #url(r'^post/(?P<pk>\d+)', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    
]

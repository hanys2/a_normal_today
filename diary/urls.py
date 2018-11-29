#blog
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^index', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^signup/$', views.signup, name='signup'),
]

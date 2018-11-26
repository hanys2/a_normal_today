from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Examples:
    # url(r'^$', 'mydiary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('diary.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
]
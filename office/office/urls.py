from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'office.views.home', name='home'),
    url(r'^', include('employment.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

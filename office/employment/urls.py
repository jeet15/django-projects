from django.conf.urls import patterns, url
from employment import views

urlpatterns = patterns('',
	url(r'^$', views.home, name= 'home'),
	#url(r'^view-employer/(?P<id>\w+)$', views.view_employer, name='view-employer'),
	url(r'^add-employer/$', views.add_employer, name='add-employer'),
	url(r'^add-education/(?P<id>\w+)$', views.add_education, name='add-education')
	)
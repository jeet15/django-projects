from django.conf.urls import patterns, url
from employment import views

urlpatterns = patterns('',
	url(r'^$', views.home, name= 'home'),
	url(r'^add-employer/$', views.add_employer, name='add-employer'),
	url(r'^view-employer/(?P<id>\w+)$', views.view_employer, name='view-employer'),
	url(r'^edit-employer/(?P<id>\w+)$', views.edit_employer, name='edit-employer'),
	url(r'^confirm-delete/(?P<id>\w+)$', views.confirm_delete, name='confirm-delete'),
	url(r'^del-profile/(?P<id>\w+)$', views.del_profile, name='del-profile'),
	#url(r'^add-education/(?P<id>\w+)$', views.add_education, name='add-education'),
	

	)
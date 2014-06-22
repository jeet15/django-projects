from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns( '', 
    url(r'^$', views.home, name= 'home'),
    url(r'^view-blog/(?P<id>\w+)$', views.view_blog, name= 'view-blog'),
    url(r'^add-comment/(?P<id>\w+)$', views.add_comment, name= 'add-comment'),
    url(r'^add-blog/$', views.add_blog, name= 'add-blog'),
    url(r'^edit-blog/(?P<id>\w+)$', views.edit_blog, name='edit-blog'),
    url(r'^confirm-blog/(?P<id>\w+)$', views.confirm_blog, name='confirm-blog'),
    url(r'^del-blog/(?P<id>\w+)$', views.del_blog, name='del-blog'),
)
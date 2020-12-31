from django.conf.urls import url, include
from . import views  

urlpatterns = [
    url(r'^shows$', views.shows),
    url(r'^shows/(?P<show_id>\d+)$', views.display_show),
    url(r'^shows/new$', views.new),
    url(r'^shows/add_show$', views.add_show),
    url(r'^shows/edit_show/(?P<show_id>\d+)$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/edit/$', views.edit_page),
    url(r'^destroy/(?P<show_id>\d+)$', views.destroy),
]
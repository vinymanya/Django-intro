from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	url(r'^(?P<number>[0-9]\d+)$', views.show),
	url(r'^(?P<blog_number>\d+)/edit$', views.edit),
	# url(r'^blogs/(\d+)/delete$', views.destroy)
]
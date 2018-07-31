from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'test$', views.test),
    url(r'new/(?P<year>[0-9]{4})/$', views.publish_year)

]
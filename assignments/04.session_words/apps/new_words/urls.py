from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^session_words$', views.session_process),
	url(r'^clear$', views.clear_session)

]
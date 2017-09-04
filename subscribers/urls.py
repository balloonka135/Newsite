from django.conf.urls import url

from . import views

app_name = 'subscribers'
urlpatterns = [
	url(r'^$', views.subscriber_new, name='sub_new'),
]
from django.conf.urls import url

from . import views

app_name = 'marketing'
urlpatterns = [
	url(r'^$', views.HomePage.as_view(), name="home"),
]
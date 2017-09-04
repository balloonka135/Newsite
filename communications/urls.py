from django.conf.urls import url

from . import views

app_name = 'communications'
urlpatterns = [
	url(r'^(?P<uuid>[\w-]+)/$', views.comm_detail, name="comm_detail"),
	url(r'^(?P<uuid>[\w-]+)/edit/$', views.comm_cru, name="comm_update"),
	url(r'^(?P<uuid>[\w-]+)/delete/$', views.CommDelete.as_view(), name="comm_delete"),
	url(r'^new/$', views.comm_cru, name="comm_new"),
]
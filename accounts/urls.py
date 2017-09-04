from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^list/$', views.AccountList.as_view(), name="account_list"),
	url(r'^(?P<uuid>[\w-]+)/$', views.account_detail, name="account_detail"),
	url(r'^new/$', views.account_cru, name='account_new'),
	url(r'^edit/$', views.account_cru, name='account_update'),
]
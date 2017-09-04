"""crmapp URL Configuration """
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^marketing/', include('marketing.urls')),
    url(r'^signup/', include('subscribers.urls')),
    url(r'^account/', include('accounts.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^comm/', include('communications.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views',
	(r'^login/$',  login),
	(r'^logout/$',  logout),
	(r'^profile/$', 'profile'),
	(r'^register/$', 'register'),
)

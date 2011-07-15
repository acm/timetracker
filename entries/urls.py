from django.conf.urls.defaults import *
from entries.models import Entry

urlpatterns = patterns('entries.views',
    (r'^$', 'index'),
	(r'^new/$', 'new'),
	(r'^(?P<entry_id>\d+)/$', 'detail'),
	(r'^edit/(?P<entry_id>\d+)/$', 'edit'),
)


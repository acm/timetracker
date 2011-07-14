from timetracker import settings
from django.conf.urls.defaults import *
#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^entries/', include('entries.urls')),
    
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
urlpatterns += patterns('django.views.static',
	(r'^static/(?P<path>.*)$', 'serve', {
		'document_root': settings.MEDIA_ROOT+settings.MEDIA_URL,
		}
	),
)
#urlpatterns += staticfiles_urlpatterns()

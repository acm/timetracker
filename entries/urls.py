from django.conf.urls.defaults import *
#from django.views.generic import DetailView, ListView
from entries.models import Entry

urlpatterns = patterns('entries.views',
    #(r'^entries/$', 'entries.views.index'),
    (r'^$', 'index'),
    #(r'^$', ListView.as_view(
    #    queryset=Entry.objects.order_by('date')[:5],
    #    context_object_name='latest_entries_list',
    #    template_name='entries/index.html')),

    #(r'^entries/(?E<entry_id>\d+)/$', 'entries.views.detail'),
)


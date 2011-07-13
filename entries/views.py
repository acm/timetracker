from django.shortcuts import render_to_response
from django.template import Context, loader
from entries.models import Entry
from django.http import HttpResponse

def index(request):
	latest_entries = ['one','two']
#	t = loader.get_template('entries/index.html')
#	c = Context({
#		'latest_entries_list': latest_entries,
#	})
#	return HttpResponse(t.render(c));
	return render_to_response('entries/index.html', {'latest_entries_list': latest_entries})

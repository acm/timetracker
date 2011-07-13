from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
from entries.models import Entry, EntryForm
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
	#twitter = urllib2.urlopen('http://twitter.co#m').read()
	latest_entries = Entry.objects.all();
#	t = loader.get_template('entries/index.html')
#	c = Context({
#		'latest_entries_list': latest_entries,
#	})
#	return HttpResponse(t.render(c));
	return render_to_response('entries/index.html', {'latest_entries_list': latest_entries})

def new(request):
	form = EntryForm(Entry)
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/entries/')
	else:
		form = EntryForm()
	return render_to_response('entries/new.html', {'form': form}, context_instance=RequestContext(request))

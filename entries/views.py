from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, loader
from entries.models import Entry, EntryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def index(request):
	#twitter = urllib2.urlopen('http://twitter.co#m').read()
	latest_entries = Entry.objects.all().order_by('date')
	return render_to_response('index.html', {'latest_entries_list': latest_entries})

def new(request):
	form = EntryForm(Entry)
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/entries/')
	else:
		form = EntryForm()
	return render_to_response(
		'new.html', 
		{'form': form, 'title': 'New Entry'}, 
		context_instance=RequestContext(request))

def edit(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)
	if request.method == 'POST':
		form = EntryForm(request.POST, instance=entry)
		if form.is_valid():
			form.save()
			request.flash['success'] = 'Entry saved successfully.'
			return HttpResponseRedirect(reverse('entries.views.edit', args=[entry.id])) 
	else:
		form = EntryForm(instance=entry)

	return render_to_response(
		'new.html', 
		{'form': form, 'title': 'Edit Entry'}, 
		context_instance=RequestContext(request))	

def detail(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)
	print entry
	return render_to_response(
		'detail.html',
		{'entry': entry},
		context_instance=RequestContext(request))

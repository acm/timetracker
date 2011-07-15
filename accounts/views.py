from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def profile(request):
	return HttpResponse('User profile for user: '+request.user.username)

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/')
	else:
		form = RegisterForm()

	return render_to_response(
		'registration/register.html', 
		{'form' : form,}, 
		context_instance=RequestContext(request),
	)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.contrib.auth import authenticate, login

from .forms import SignupForm

# Create your views here.

def signup(request):

	if request.method == "POST":
	
		signup_form = SignupForm(request.POST)
		
		if signup_form.is_valid():
			
			signup_form.save()
			
			username = request.POST['username']
			password = request.POST['password']
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				
				login(request, user)
				
				return HttpResponseRedirect('/')
			
	else:
		
		signup_form = SignupForm()
		
	return render( request, 'signup.html', {'signup': signup_form})

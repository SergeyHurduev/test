# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.core.paginator import Paginator

from .models import Question
from .models import Answer
from .forms import AnswerForm, AskForm
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def news(request, *args, **kwargs):
	
	try:
		limit = int(request.GET.get('limit', 10))
		if limit < 0 or limit > 100:
			limit = 10
	except:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
		if page < 0:
			page = 1
	except:
		page = 1
	
	paginator = Paginator(Question.objects.new(), limit)
	paginator.baseurl = "?page="
	questions = paginator.page(page)
	
	
	username = request.user if request.user != "AnonymousUser" else None
	 
	return render( request, 'news.html', {
		'username': username,
		'questions': questions,
		'paginator': paginator,
		'page': page
	})

def popular(request, *args, **kwargs):
	
	try:
		limit = int(request.GET.get('limit', 10))
		if limit < 0 or limit > 100:
			limit = 10
	except:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
		if page < 0:
			page = 1
	except:
		page = 1
	
	paginator = Paginator(Question.objects.popular(), limit)
	paginator.baseurl = "?page="
	questions = paginator.page(page)
	
	return render( request, 'popular.html', {
		'questions': questions,
		'paginator': paginator,
		'page': page
	})

def question(request, _id):
	
	question = get_object_or_404(Question,id=_id)
	answers = Answer.objects.filter(question_id=_id).order_by('-id')
	
	if request.method == "POST":
		
		answer_form = AnswerForm(request.POST)
		answer_form._user = request.user
		
		if answer_form.is_valid():
			
			answer = answer_form.save()
			
			return HttpResponseRedirect('/question/%s' % _id)
			
	else:
		
		data = {'question':_id}
		
		answer_form = AnswerForm(initial=data)
		
		
	return render( request, 'question.html', {
		'question': question,
		'answers': answers,
		'answer_form': answer_form
	})

def ask(request):

	if request.method == "POST":
	
		ask_form = AskForm(request.POST)
		ask_form._user = request.user
		
		if ask_form.is_valid():
			
			ask = ask_form.save()
			return HttpResponseRedirect('/question/%s' % ask.id)
			
	else:
		
		ask_form = AskForm()
		
	return render( request, 'ask.html', {'ask_form': ask_form})

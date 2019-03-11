# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.core.paginator import Paginator

from .models import Question
from .models import Answer
from .forms import AnswerForm

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect 

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
	
	return render( request, 'news.html', {
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
	answers = Answer.objects.filter(question_id=_id)
	
	if request.method == "POST":
		
		answer_form = AnswerForm(request.POST)
		
		if answer_form.is_valid():
			
			answer = answer_form.save()
			return HttpResponseRedirect('qquestion/%s' % _id)
			
	else:
		
		data = {'question':_id, 'author': None}
		
		answer_form = AnswerForm(initial=data)
		
		
	return render( request, 'question.html', {
		'question': question,
		'answers': answers,
		'answer_form': answer_form
	})


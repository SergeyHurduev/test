# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator

from .models import Question
from .models import Answer

# Create your views here.

from django.http import HttpResponse 

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

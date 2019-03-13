# -*- coding: utf-8 -*-

from .models import Answer, Question
from django import forms
from django.contrib.auth.models import User

#class AskForm(ModelForm):
#	class Meta:
#		model = Question
#		fields = ['title', 'text']
#	

class AnswerForm(forms.Form):
	
	text = forms.CharField(label='text', widget = forms.Textarea)
	question = forms.IntegerField(widget = forms.widgets.HiddenInput)
	author = forms.CharField(widget = forms.widgets.HiddenInput, required = False)
	
	def save(self):
		
		text = self.cleaned_data['text']
		question = Question.objects.get(id=self.cleaned_data['question'])
		
		try:
			author = User.objects.get(username=self.cleaned_data['author'])
		except User.DoesNotExist:
			author = None
		
		answer = Answer(text=text, question=question, author=author)
		
		answer.save()
		
		return answer

class AskForm(forms.Form):

	title = forms.CharField(label='title', max_length=100)
	text = forms.CharField(label='text', widget = forms.Textarea)
	
	author = forms.CharField(widget = forms.widgets.HiddenInput, required = False)
	
	def save(self):
		
		text = self.cleaned_data['text']
		title = self.cleaned_data['title']
		
		try:
			author = User.objects.get(username=self.cleaned_data['author'])
		except User.DoesNotExist:
			author = None
		
		ask = Question(title=title, text=text, author=author)
		
		ask.save()
		
		return ask
		
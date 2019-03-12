# -*- coding: utf-8 -*-

from .models import Answer, Question
from django import forms
#class AskForm(ModelForm):
#	class Meta:
#		model = Question
#		fields = ['title', 'text']
#	

class AnswerForm(forms.Form):
	
	text = forms.CharField(label='text', widget = forms.Textarea)
	question = forms.IntegerField(widget = forms.widgets.HiddenInput)
	author = forms.InetegerField(widget = forms.widgets.HiddenInput, required = False)
	
	def save(self):
		text = self.cleaned_data['text']
		question = Question.objects.get(id=self.cleaned_data['question'])
		answer = Answer(text=text,question=question)
		answer.save()
		return answer

class AskForm(forms.Form):

	title = forms.CharField(label='title', max_length=100)
	text = forms.CharField(label='text', widget = forms.Textarea)
	
	def save(self):
		text = self.cleaned_data['text']
		title = self.cleaned_data['title']
		ask = Question(title=title, text=text)
		ask.save()
		return ask

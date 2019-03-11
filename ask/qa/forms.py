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
	question = forms.CharField(widget = forms.widgets.HiddenInput)
	author = forms.CharField(widget = forms.widgets.HiddenInput, required = False)
	
	def save(self):
		text = self.cleaned_data['text']
		question = Question.objects.get(id=self.cleaned_data['question'])
		answer = Answer(text=text,question=question)
		answer.save()
		return answer


# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
	
	username = forms.CharField(label='username', max_length=32)
	email = forms.EmailField(label='email', max_length=60)
	password = forms.CharField(label='password', widget=forms.PasswordInput)
	
	def save(self):
		
		username = self.cleaned_data['username']
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		
		user = User.objects.create_user(username, email = email, password = password)
		
		return user


class LoginForm(forms.Form):
	
	username = forms.CharField(label='username', max_length=32)
	password = forms.CharField(label='password', widget=forms.PasswordInput)
	



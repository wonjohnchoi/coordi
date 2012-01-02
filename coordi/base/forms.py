# -*- coding: utf-8 -*-

'''
Created on Dec 20, 2011

@author: wonjohnchoi
'''
from django import forms
from django.contrib.auth.models import User
class UserField(forms.CharField):
    def clean(self, value):
        super(UserField, self).clean(value)
        try:
            User.objects.get(username=value)
            raise forms.ValidationError("Someone is already using this username. Please pick another.")
        except User.DoesNotExist:
            return value
import re
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = UserField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repeat your password")
    email = forms.EmailField()
    email2 = forms.EmailField(label="Repeat your email")
    def clean_username(self):
        if re.search(r'^[a-zA-Z0-9]+(.[a-zA-Z0-9]+)*$', self.data['username']) is None:
            raise forms.ValidationError('User name must only have alphabets and non-consecutive dots.')
        return self.data['username']
    def clean_email(self):
        if self.data['email'] != self.data['email2']:
            raise forms.ValidationError('Emails are not the same')
        try:
            User.objects.get(email=self.data['email'])
            raise forms.ValidationError("Someone is already using this email. Please pick another.")
        except User.DoesNotExist:
            return self.data['email']

    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password']
    
    def clean(self,*args, **kwargs):
        self.clean_email()
        self.clean_password()
        self.clean_username()
        return super(SignupForm, self).clean(*args, **kwargs)

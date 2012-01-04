# -*- coding: utf-8 -*-

'''
Created on Dec 20, 2011

@author: wonjohnchoi
'''
from django import forms
from django.contrib.auth.models import User
from coordi.base.models import Promocode
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
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    email2 = forms.EmailField()
    #birthday = forms.
    #gender
    photo = forms.ImageField(max_length = 500, required=False)
    promocode = forms.CharField(max_length=35, required = False)
    
    def clean_username(self):
        if re.search(r'^[a-zA-Z0-9]+(.[a-zA-Z0-9]+)*$', self.data['username']) is None:
            raise forms.ValidationError('User name must only have alphabets, numbers, and non-consecutive dots.')
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
    def clean_promocode(self):
        if self.data['promocode'] == '':
            return ''
        try:
            Promocode.objects.get(promocode_id = self.data['promocode'])
            return self.data['promocode']
        except Promocode.DoesNotExist:
            raise forms.ValidationError('Promocode does not exist')
    def clean(self,*args, **kwargs):
        self.clean_email()
        self.clean_password()
        self.clean_username()
        self.clean_promocode()
        return super(SignupForm, self).clean(*args, **kwargs)

class WallPostForm(forms.Form):
    post = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':'5','cols':'70'}), min_length=1)
    

    def clean_post(self):
        if not (1 <= len(self.data['post']) <= 500):
            raise forms.ValidationError('Must be less or equal to 500 characters')
        return self.data['post']
    
    def clean(self,*args, **kwargs):
        self.clean_post()
        return super(WallPostForm, self).clean(*args, **kwargs)

class WallCommentForm(forms.Form):
    comment = forms.CharField(max_length=100, widget=forms.Textarea, min_length=1)
    

    def clean_comment(self):
        if not (1 <= len(self.data['comment']) <= 100):
            raise forms.ValidationError('Must be less or equal to 500 characters')
        return self.data['comment']
    
    def clean(self,*args, **kwargs):
        self.clean_comment()
        return super(WallCommentForm, self).clean(*args, **kwargs)
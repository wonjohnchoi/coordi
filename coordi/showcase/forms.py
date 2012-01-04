# -*- coding: utf-8 -*-

'''
Created on Dec 20, 2011

@author: wonjohnchoi
'''
from django import forms
from django.contrib.auth.models import User
from coordi.base.models import Promocode
class EntryForm(forms.Form):
    photo = forms.ImageField(max_length = 500)
    text = forms.CharField(widget=forms.Textarea, required = False)
    

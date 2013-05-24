# -*- coding: utf-8 -*-

from django import forms

class FormDocument(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    format = forms.CharField(max_length=20)
    title = forms.CharField(max_length=100)
    description = forms.TextInput()


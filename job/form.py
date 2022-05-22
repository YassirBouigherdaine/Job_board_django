from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Candidate, Job


class ApplyForm(forms.ModelForm):
     
     class Meta:
         model = Candidate
         fields = ['name','email','website','cv','coverLetter']


class JobForm(forms.ModelForm):
     
     class Meta:
         model = Job
         fields = '__all__'
         exclude = {'slug','user',}
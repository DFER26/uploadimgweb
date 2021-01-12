# forms.py
from django import forms
from .models import *

class image_Form(forms.ModelForm):

    class Meta:
        model = images
        fields = ['name', 'Main_Img', 'Snd_Img']
        labels = {'name':'Agent', 'Main_Img':'Front IC', 'Snd_Img':'Back IC'}

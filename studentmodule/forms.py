from django import forms

from .models import *


class courseapplicationform(forms.ModelForm):
    class Meta:
      model=courseapplication
      fields= ['name','email','certificate']
    def __init__(self, *args, **kwargs):
        super(courseapplicationform,self).__init__(*args, **kwargs)
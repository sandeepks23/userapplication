from django import forms
from django.forms import ModelForm
from .models import Posts
# class AddObjects(forms.Form):
#     name=forms.CharField()

class AddPost(ModelForm):
    class Meta:
        model=Posts
        fields=['text_content']
        widgets={
            'text_content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your thoughts!'})

        }



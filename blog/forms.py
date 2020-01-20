from django import forms
from .models import Blog
class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Aa'
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
    }))
    class Meta:
        model =Blog
        fields = '__all__'

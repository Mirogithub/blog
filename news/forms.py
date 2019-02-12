from django import forms
from .models import Article, Tag
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description', 'text', 'category', 'photo_main', 'tags']
        required = ['name', 'description', 'text', 'category', 'photo_main']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

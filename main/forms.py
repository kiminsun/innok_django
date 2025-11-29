"""
폼 정의
"""
from django import forms
from .models import Notice, Estimate, FAQ


class NoticeForm(forms.ModelForm):
    """공지사항 폼"""
    class Meta:
        model = Notice
        fields = ['title', 'author', 'content', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class EstimateForm(forms.ModelForm):
    """견적문의 폼"""
    class Meta:
        model = Estimate
        fields = ['title', 'author', 'password', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class FAQForm(forms.ModelForm):
    """FAQ 폼"""
    class Meta:
        model = FAQ
        fields = ['title', 'author', 'password', 'question', 'answer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


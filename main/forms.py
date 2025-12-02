"""
폼 정의 - 다국어 지원
"""
from django import forms
from django.utils.translation import get_language
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 현재 언어에 따라 라벨 설정
        if get_language() == 'en':
            self.fields['title'].label = 'Title'
            self.fields['author'].label = 'Author'
            self.fields['content'].label = 'Content'
            self.fields['attachment'].label = 'Attachment'
            # placeholder 설정
            self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
            self.fields['author'].widget.attrs['placeholder'] = 'Enter your name'
            self.fields['content'].widget.attrs['placeholder'] = 'Enter content'


class EstimateForm(forms.ModelForm):
    """견적문의 폼 - 다국어 지원"""
    class Meta:
        model = Estimate
        fields = ['title', 'author', 'password', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 현재 언어에 따라 라벨 설정
        if get_language() == 'en':
            self.fields['title'].label = 'Title'
            self.fields['author'].label = 'Author'
            self.fields['password'].label = 'Password'
            self.fields['content'].label = 'Content'
            # placeholder 설정
            self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
            self.fields['author'].widget.attrs['placeholder'] = 'Enter your name'
            self.fields['password'].widget.attrs['placeholder'] = 'Enter password for editing/deleting'
            self.fields['content'].widget.attrs['placeholder'] = 'Enter your inquiry details'
        else:
            # 한국어 placeholder 설정
            self.fields['title'].widget.attrs['placeholder'] = '제목을 입력하세요'
            self.fields['author'].widget.attrs['placeholder'] = '이름을 입력하세요'
            self.fields['password'].widget.attrs['placeholder'] = '수정/삭제 시 사용할 비밀번호'
            self.fields['content'].widget.attrs['placeholder'] = '문의 내용을 입력하세요'


class FAQForm(forms.ModelForm):
    """FAQ 폼 - 다국어 지원"""
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 현재 언어에 따라 라벨 설정
        if get_language() == 'en':
            self.fields['title'].label = 'Title'
            self.fields['author'].label = 'Author'
            self.fields['password'].label = 'Password'
            self.fields['question'].label = 'Question'
            self.fields['answer'].label = 'Answer'
            # placeholder 설정
            self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
            self.fields['author'].widget.attrs['placeholder'] = 'Enter your name'
            self.fields['password'].widget.attrs['placeholder'] = 'Enter password for editing/deleting'
            self.fields['question'].widget.attrs['placeholder'] = 'Enter your question'
            self.fields['answer'].widget.attrs['placeholder'] = 'Enter answer (admin only)'

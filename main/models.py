"""
게시판 모델 정의
"""
from django.db import models
from django.utils import timezone


class Notice(models.Model):
    """공지사항 모델"""
    title = models.CharField(max_length=255, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    content = models.TextField(verbose_name='내용')
    views = models.IntegerField(default=0, verbose_name='조회수')
    attachment = models.FileField(upload_to='notices/', blank=True, null=True, verbose_name='첨부파일')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Estimate(models.Model):
    """견적문의 모델"""
    title = models.CharField(max_length=255, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    password = models.CharField(max_length=255, verbose_name='비밀번호')
    content = models.TextField(verbose_name='내용')
    views = models.IntegerField(default=0, verbose_name='조회수')
    answer = models.TextField(blank=True, null=True, verbose_name='답변')
    answered_at = models.DateTimeField(blank=True, null=True, verbose_name='답변일자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        verbose_name = '견적문의'
        verbose_name_plural = '견적문의'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def set_answer(self, answer_text):
        """답변 설정"""
        self.answer = answer_text
        self.answered_at = timezone.now()
        self.save()


class FAQ(models.Model):
    """자주하는 질문 모델"""
    title = models.CharField(max_length=255, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    password = models.CharField(max_length=255, verbose_name='비밀번호')
    question = models.TextField(verbose_name='질문')
    answer = models.TextField(blank=True, null=True, verbose_name='답변')
    views = models.IntegerField(default=0, verbose_name='조회수')
    answered_at = models.DateTimeField(blank=True, null=True, verbose_name='답변일자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        verbose_name = '자주하는 질문'
        verbose_name_plural = '자주하는 질문'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def set_answer(self, answer_text):
        """답변 설정"""
        self.answer = answer_text
        self.answered_at = timezone.now()
        self.save()

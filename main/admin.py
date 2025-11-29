"""
관리자 페이지 설정
"""
from django.contrib import admin
from .models import Notice, Estimate, FAQ


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """공지사항 관리자"""
    list_display = ('title', 'author', 'views', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at')


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    """견적문의 관리자"""
    list_display = ('title', 'author', 'views', 'answered_at', 'created_at')
    list_filter = ('created_at', 'answered_at')
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at', 'answered_at')
    
    fieldsets = (
        ('문의 정보', {
            'fields': ('title', 'author', 'password', 'content')
        }),
        ('답변 정보', {
            'fields': ('answer', 'answered_at')
        }),
        ('통계', {
            'fields': ('views', 'created_at', 'updated_at')
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """FAQ 관리자"""
    list_display = ('title', 'author', 'views', 'answered_at', 'created_at')
    list_filter = ('created_at', 'answered_at')
    search_fields = ('title', 'question', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at', 'answered_at')
    
    fieldsets = (
        ('질문 정보', {
            'fields': ('title', 'author', 'password', 'question')
        }),
        ('답변 정보', {
            'fields': ('answer', 'answered_at')
        }),
        ('통계', {
            'fields': ('views', 'created_at', 'updated_at')
        }),
    )

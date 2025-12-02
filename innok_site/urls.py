"""
URL configuration for innok_site project.
다국어 지원을 위해 i18n_patterns 사용

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# 언어 prefix가 필요 없는 URL (관리자, 미디어 등)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('innokadm/', include('admin_panel.urls')),
    path('i18n/', include('django.conf.urls.i18n')),  # 언어 전환 URL
]

# 다국어 지원 URL (언어 prefix 적용: /ko/, /en/)
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    prefix_default_language=False,  # 기본 언어(한국어)는 prefix 없이 접근 가능
)

# 개발 환경에서 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

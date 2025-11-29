"""
관리자 패널 URL 설정
"""
from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_login, name='login'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.manage_projects, name='manage_projects'),
    path('projects/download/', views.download_projects_json, name='download_projects_json'),
    path('about/', views.manage_about, name='manage_about'),
    path('contact/', views.manage_contact, name='manage_contact'),
]


"""
메인 뷰 함수 - 다국어 지원
"""
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.translation import get_language
from .models import Notice, Estimate, FAQ
import json
import os
from django.conf import settings


def get_json_data_path(filename):
    """
    현재 언어에 따라 JSON 데이터 파일 경로를 반환
    영문 버전이 없으면 기본 한국어 버전 반환
    """
    lang = get_language()
    if lang == 'en':
        en_path = settings.JSON_DATA_DIR / 'en' / filename
        if os.path.exists(en_path):
            return en_path
    # 기본 한국어 버전 반환
    return settings.JSON_DATA_DIR / filename


def index(request):
    """메인 페이지"""
    lang = get_language()
    return render(request, 'main/index.html', {'lang': lang})


def business(request):
    """사업소개 페이지 - 다국어 지원"""
    lang = get_language()
    
    # JSON 형식 요청 처리
    if request.GET.get('format') == 'json':
        from django.http import JsonResponse
        json_path = get_json_data_path('projects.json')
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 특정 프로젝트 상세 정보 요청
            project_id = request.GET.get('id')
            project_type = request.GET.get('type')
            if project_id and project_type:
                projects = data.get(project_type, [])
                project = next((p for p in projects if p.get('id') == int(project_id)), None)
                if project:
                    return JsonResponse(project)
                return JsonResponse({'error': 'Project not found'}, status=404)
            
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'main/business.html', {'lang': lang})


def about(request):
    """회사소개 페이지 - 다국어 지원"""
    lang = get_language()
    
    # 회사소개 데이터 로드
    json_path = get_json_data_path('about.json')
    about_data = {}
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            about_data = json.load(f)
    except Exception:
        pass
    
    return render(request, 'main/about.html', {'lang': lang, 'about_data': about_data})


def contact(request):
    """고객센터 페이지 - 다국어 지원"""
    lang = get_language()
    
    # 연락처 데이터 로드
    json_path = get_json_data_path('contact.json')
    contact_data = {}
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            contact_data = json.load(f)
    except Exception:
        pass
    
    return render(request, 'main/contact.html', {'lang': lang, 'contact_data': contact_data})


def notice_list(request):
    """공지사항 목록"""
    notices = Notice.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        notices = notices.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(notices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/notice_list.html', context)


def notice_detail(request, pk):
    """공지사항 상세보기"""
    notice = Notice.objects.get(pk=pk)
    notice.views += 1
    notice.save()
    return render(request, 'main/notice_detail.html', {'notice': notice})


def estimate_list(request):
    """견적문의 목록"""
    estimates = Estimate.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        estimates = estimates.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(estimates, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/estimate_list.html', context)


def estimate_create(request):
    """견적문의 작성"""
    from .forms import EstimateForm
    
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save()
            return redirect('main:estimate_detail', pk=estimate.pk)
    else:
        form = EstimateForm()
    
    return render(request, 'main/estimate_create.html', {'form': form})


def estimate_detail(request, pk):
    """견적문의 상세보기"""
    try:
        estimate = Estimate.objects.get(pk=pk)
    except Estimate.DoesNotExist:
        return redirect('main:estimate_list')
    
    # 비밀번호 확인
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == estimate.password:
            estimate.views += 1
            estimate.save()
            return render(request, 'main/estimate_detail.html', {'estimate': estimate})
        else:
            error_message = '비밀번호가 올바르지 않습니다.'
            return render(request, 'main/estimate_detail.html', 
                         {'estimate': estimate, 'error_message': error_message})
    
    return render(request, 'main/estimate_detail.html', {'estimate': estimate})


def faq_list(request):
    """FAQ 목록"""
    faqs = FAQ.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        faqs = faqs.filter(
            Q(title__icontains=search_query) | 
            Q(question__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(faqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/faq_list.html', context)


def faq_detail(request, pk):
    """FAQ 상세보기"""
    faq = FAQ.objects.get(pk=pk)
    
    # 비밀번호 확인
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == faq.password:
            faq.views += 1
            faq.save()
            return render(request, 'main/faq_detail.html', {'faq': faq})
        else:
            error_message = '비밀번호가 올바르지 않습니다.'
            return render(request, 'main/faq_detail.html', 
                         {'faq': faq, 'error_message': error_message})
    
    return render(request, 'main/faq_detail.html', {'faq': faq})


def pr_center(request):
    """PR CENTER 페이지"""
    return render(request, 'main/pr_center.html')

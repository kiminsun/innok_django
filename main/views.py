"""
메인 뷰 함수
"""
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Notice, Estimate, FAQ
import json
import os
from django.conf import settings


def index(request):
    """메인 페이지"""
    return render(request, 'main/index.html')


def business(request):
    """사업소개 페이지"""
    return render(request, 'main/business.html')


def about(request):
    """회사소개 페이지"""
    return render(request, 'main/about.html')


def contact(request):
    """고객센터 페이지"""
    return render(request, 'main/contact.html')


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

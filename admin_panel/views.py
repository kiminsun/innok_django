"""
관리자 패널 뷰
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
import os


def admin_login(request):
    """관리자 로그인"""
    if request.user.is_authenticated:
        return redirect('admin_panel:dashboard')
    
    from django import forms
    
    class LoginForm(forms.Form):
        username = forms.CharField(label='사용자명', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_panel:dashboard')
            else:
                error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
                return render(request, 'admin_panel/login.html', {'form': form, 'error_message': error_message})
        else:
            return render(request, 'admin_panel/login.html', {'form': form})
    else:
        form = LoginForm()
    
    return render(request, 'admin_panel/login.html', {'form': form})


@login_required
def admin_logout(request):
    """관리자 로그아웃"""
    logout(request)
    return redirect('admin_panel:login')


@login_required
def dashboard(request):
    """관리자 대시보드"""
    return render(request, 'admin_panel/dashboard.html')


@login_required
def manage_projects(request):
    """사업소개 데이터 관리"""
    json_path = settings.JSON_DATA_DIR / 'projects.json'
    
    # JSON 데이터 디렉토리 생성
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    # GET 요청 시 JSON 데이터 반환
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {
            "specialized": [],
            "general": [],
            "education": [],
            "regulatory": [],
            "m&a": []
        }
        # 기본 파일 생성
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 템플릿에서 JSON 사용 가능하도록 변환
    from django.utils.safestring import mark_safe
    import django.utils.safestring as safe
    
    return render(request, 'admin_panel/manage_projects.html', {
        'data': data,
        'data_json': mark_safe(json.dumps(data))
    })


@login_required
def download_projects_json(request):
    """프로젝트 JSON 다운로드"""
    json_path = settings.JSON_DATA_DIR / 'projects.json'
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            response = HttpResponse(f.read(), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="projects.json"'
            return response
    return JsonResponse({'error': '파일이 없습니다.'})


@login_required
def manage_about(request):
    """회사소개 데이터 관리"""
    json_path = settings.JSON_DATA_DIR / 'about.json'
    
    # JSON 데이터 디렉토리 생성
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {
            "companySlogan": "보건복지부, 식약처, 교육부 등 다양한 정부 기관에서 쌓은, 23년간의 광범위한 약무행정실무 경력을 바탕으로, 차별·특화된 전문 맞춤 상담을 통하여, 고객의 의뢰에 대한 최선의 해답을 제시해 드리겠습니다.",
            "representativeImage": "",
            "history": [],
            "organization": {}
        }
        # 기본 파일 생성
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 템플릿에서 JSON 사용 가능하도록 변환
    from django.utils.safestring import mark_safe
    import json as json_module
    return render(request, 'admin_panel/manage_about.html', {
        'data': data,
        'data_json': mark_safe(json_module.dumps(data.get('organization', {}), ensure_ascii=False))
    })


@login_required
def manage_contact(request):
    """고객센터 데이터 관리"""
    json_path = settings.JSON_DATA_DIR / 'contact.json'
    
    # JSON 데이터 디렉토리 생성
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {
            "businessHours": "평일 오전 10시 ~ 오후 5시",
            "phone": "02-756-7094",
            "mobile": "010-7131-7094",
            "fax": "0504-207-7094",
            "email": "innogi2020@innok.kr",
            "address": "서울특별시 용산구 두텁바위로 58길 7, 630호(장우빌딩)",
            "instagram": "https://www.instagram.com/innok_corporation/",
            "blog": "https://blog.naver.com/iosis1218"
        }
        # 기본 파일 생성
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return render(request, 'admin_panel/manage_contact.html', {'data': data})


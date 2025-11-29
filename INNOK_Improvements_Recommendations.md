# INNOK 홈페이지 프롬프트 개선사항 및 추천

## 📝 주요 개선사항

### 1. 기술 스택 명확화
**원본**: "html,css,bootstrap,django프레임워크,mysql를 이용해서 다양하게 활용"
**개선**: 
- 명확한 버전 명시 (Bootstrap 5, Django 4.x, MySQL 8.0)
- JavaScript 프레임워크 명시 (바닐라 JS 또는 선택적 프레임워크)
- 추가 라이브러리 제안 (AOS, GSAP, Swiper.js 등)

### 2. 데이터 구조 구체화
**추가 내용**:
- JSON 파일 구조 예시 제공
- MySQL 테이블 스키마 상세 정의
- 각 필드의 데이터 타입 및 제약조건 명시

### 3. 보안 강화
**추가 고려사항**:
- SQL Injection 방지 (Django ORM 활용)
- XSS 방지 (이스케이프 처리)
- CSRF 토큰 사용
- 비밀번호 암호화 (bcrypt)
- 관리자 페이지 접근 제한
- 세션 타임아웃 설정

### 4. 성능 최적화
**추가 사항**:
- 이미지 최적화 (WebP 형식, 레이지 로딩)
- CSS/JS 파일 압축 및 미니파이
- CDN 활용
- 데이터베이스 인덱싱
- 캐싱 전략

### 5. SEO 및 접근성
**추가 항목**:
- 메타 태그 구성
- Open Graph 태그 (SNS 공유 최적화)
- 구조화된 데이터 (JSON-LD)
- 사이트맵 생성
- ARIA 레이블
- 키보드 네비게이션 지원

---

## 🎨 디자인 개선사항

### 컬러 팔레트 제안
- 메인: 전문성과 신뢰를 주는 블루 계열
- 서브: 의료/제약 산업을 상징하는 화이트/그레이
- 액센트: 포인트 컬러 (예: 티얼 그린, 딥 블루)

### 타이포그래피
- 한글: 본고딩, Noto Sans KR
- 영문/숫자: Inter, Roboto
- 적절한 폰트 크기 및 행간

### 반응형 브레이크포인트
- 모바일: 320px ~ 768px
- 태블릿: 769px ~ 1024px
- 데스크톱: 1025px 이상

---

## 🚀 기능 추가 추천

### 필수 기능
1. **지도 API 연동**: 네이버 지도 또는 카카오맵으로 고객센터 위치 표시
2. **연락처 바로가기**: 전화번호 클릭 시 전화 걸기, 이메일 클릭 시 메일 보내기
3. **검색 기능**: 사업소개 섹션에서 프로젝트 검색
4. **이미지 갤러리**: Lightbox 효과로 이미지 확대 보기
5. **스크롤 인디케이터**: 현재 위치 표시

### 선택 기능
1. **다국어 지원**: 한국어/영어 전환
2. **다크 모드**: 사용자 선택 가능한 다크 모드
3. **뉴스레터 구독**: 이메일 수집 및 구독 기능
4. **실시간 채팅**: 고객 상담 챗봇 연동
5. **Google Analytics**: 방문자 분석
6. **프린트 스타일**: 인쇄 시 최적화된 스타일

---

## 🔧 기술적 추천사항

### Django 고려사항
**문제점**: Django는 서버 사이드 프레임워크인데 GitHub Pages는 정적 사이트 호스팅

**해결 방안**:
1. **옵션 A (권장)**: Django를 API 서버로 사용, 프론트엔드는 정적 사이트
   - Django: 관리자 페이지 및 API만 제공
   - 프론트엔드: 정적 HTML/CSS/JS로 빌드
   - 배포: GitHub Pages (프론트엔드) + 별도 호스팅 (Django API)

2. **옵션 B**: 완전 정적 사이트로 변경
   - Django 대신 순수 JavaScript로 관리자 기능 구현
   - 데이터는 JSON 파일로 관리
   - Firebase 또는 Supabase로 백엔드 대체

3. **옵션 C**: Django를 전체 서버로 배포
   - GitHub Pages 대신 Heroku, AWS, DigitalOcean 등 사용
   - Django 전체 기능 활용 가능

### 데이터베이스 고려사항
**문제점**: MySQL을 GitHub Pages에 직접 연결 불가

**해결 방안**:
1. **원격 MySQL**: 
   - AWS RDS, PlanetScale, 또는 다른 클라우드 MySQL 서비스 사용
   - Django API 서버에서 연결

2. **대안 데이터베이스**:
   - SQLite (소규모 프로젝트용, 단 GitHub Pages에서 직접 사용 불가)
   - Firebase Firestore (NoSQL)
   - Supabase (PostgreSQL)

### GitHub Actions 워크플로우 제안
```yaml
name: Build and Deploy
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Collect static files
        run: |
          python manage.py collectstatic --noinput
      - name: Build static site
        run: |
          # 정적 사이트 빌드 스크립트
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

---

## 📊 개발 단계별 체크리스트

### Phase 1: 기획 및 설계
- [ ] 와이어프레임 작성
- [ ] 디자인 목업 작성
- [ ] 데이터베이스 스키마 설계
- [ ] API 설계 (필요 시)

### Phase 2: 개발
- [ ] 개발 환경 설정
- [ ] Django 프로젝트 초기화
- [ ] 모델 생성 및 마이그레이션
- [ ] 관리자 페이지 개발
- [ ] 프론트엔드 레이아웃 구성
- [ ] 각 섹션 구현
- [ ] 반응형 디자인 적용
- [ ] 애니메이션 및 인터랙션 추가

### Phase 3: 테스트
- [ ] 기능 테스트
- [ ] 반응형 테스트
- [ ] 브라우저 호환성 테스트
- [ ] 보안 테스트
- [ ] 성능 테스트

### Phase 4: 배포
- [ ] GitHub Actions 워크플로우 구성
- [ ] 프로덕션 환경 설정
- [ ] 배포 및 검증

---

## 🎯 우선순위 권장사항

### 높은 우선순위 (필수)
1. 반응형 디자인 구현
2. 보안 조치 (인증, 암호화)
3. 관리자 페이지 기본 기능
4. 데이터베이스 연동
5. 기본 SEO 설정

### 중간 우선순위 (권장)
1. 애니메이션 효과
2. 이미지 최적화
3. 검색 기능
4. 지도 API 연동
5. 성능 최적화

### 낮은 우선순위 (선택)
1. 다국어 지원
2. 다크 모드
3. 뉴스레터
4. 실시간 채팅
5. 고급 분석 도구

---

## 💡 추가 팁

1. **프로토타입 먼저**: 전체 구조를 빠르게 프로토타입으로 만들어 테스트
2. **점진적 개선**: 핵심 기능부터 구현 후 점진적으로 기능 추가
3. **사용자 피드백**: 초기 버전 배포 후 사용자 피드백 수집
4. **백업 전략**: 정기적인 데이터 백업 계획 수립
5. **문서화**: 코드 및 관리자 매뉴얼 작성

---

이 문서는 프롬프트 개선 시 참고용으로 작성되었습니다.


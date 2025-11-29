# INNOK 홈페이지 제작 프롬프트

## 프로젝트 개요
**목적**: innok.kr 의료제품 GMP 교육 및 컨설팅 회사 공식 홈페이지 제작
**회사명**: INNOK
**사업분야**: 의료제품 GMP 교육 및 컨설팅

---

## 페이지 구성

### 1. 메인 페이지 (INNOK)
- **디자인 요구사항**:
  - 전체 배경을 회사 홍보 이미지로 구성 (2개 이미지 교차 배치 또는 슬라이더)
  - 이미지 위에 회사의 상징적인 멘트/슬로건 오버레이
  - 메인 화면으로 사용되는 히어로 섹션

### 2. 사업소개 (Business)
총 5가지 사업 영역을 섹션으로 구성:

#### 2.1 특화사업
- 갤러리 형식으로 프로젝트 카드 나열
- 각 항목 클릭 시 상세보기 모달/팝업 표시
- 프로젝트 정보: 제목, 설명, 이미지, 기간 등

#### 2.2 일반사업
- 갤러리 형식으로 프로젝트 카드 나열
- 각 항목 클릭 시 상세보기 모달/팝업 표시

#### 2.3 교육사업
- 갤러리 형식으로 프로젝트 카드 나열
- 각 항목 클릭 시 상세보기 모달/팝업 표시

#### 2.4 규제전문 에이전시
- 갤러리 형식으로 프로젝트 카드 나열
- 각 항목 클릭 시 상세보기 모달/팝업 표시

#### 2.5 브랜딩 지원 사업(M&A)
- 갤러리 형식으로 프로젝트 카드 나열
- 각 항목 클릭 시 상세보기 모달/팝업 표시

**공통 기능**:
- 각 사업별 필터링 기능
- 검색 기능
- 이미지 레이지 로딩
- 무한 스크롤 또는 페이지네이션

### 3. 회사소개 (About)
- 회사를 표현하는 한 문장 멘트:
  > "보건복지부, 식약처, 교육부 등 다양한 정부 기관에서 쌓은, 23년간의 광범위한 약무행정실무 경력을 바탕으로, 차별·특화된 전문 맞춤 상담을 통하여, 고객의 의뢰에 대한 최선의 해답을 제시해 드리겠습니다."
- 대표 이미지 포함
- 회사 연혁, 조직도 등 추가 정보 섹션 구성 권장

### 4. 고객센터 (Contact)
다음 정보를 깔끔하게 표현:

**연락처 정보**:
- 업무시간: 평일 오전 10시 ~ 오후 5시
- 대표번호: 02-756-7094
- 핸드폰: 010-7131-7094
- FAX: 0504-207-7094
- EMAIL: innogi2020@innok.kr
- 주소: 장우빌딩 서울특별시 용산구 후암동 339-4, 630호

**SNS 링크**:
- 인스타그램: https://www.instagram.com/innok_corporation/
- 네이버 블로그: https://blog.naver.com/iosis1218

**추가 권장사항**:
- 지도 API 연동 (네이버 지도 또는 카카오맵)
- 연락처 클릭 시 전화 걸기, 이메일 보내기 기능

### 5. 공지사항 (Notice)
- 게시판 형식
- 컬럼: 번호, 제목, 글쓴이, 조회수, 등록일자
- 상세보기 페이지
- 페이지네이션

### 6. 견적문의 (Estimate)
- 질문답변 게시판 형식
- 컬럼: 번호, 제목, 글쓴이, 비밀번호, 조회수, 등록일자
- 비밀번호로 본인 게시글 확인
- 상세보기 페이지
- 페이지네이션

### 7. 자주하는 질문 (FAQ)
- 질문답변 게시판 형식
- 컬럼: 번호, 제목, 글쓴이, 비밀번호, 조회수, 등록일자, 답변일자
- 아코디언 형식으로 Q&A 표시 (추천)
- 관리자가 답변 가능하도록 구성
- 페이지네이션

### 8. PR CENTER
- 관련 동영상 링크 (YouTube 임베드)
- 관련 사진 갤러리 (링크 또는 직접 업로드)

### 9. 푸터 (Footer)
다음 링크들을 포함:
- 식약처 링크
- 정부24 링크
- 의약품안전나라 링크
- HIRA 링크
- NECA 링크
- 이노케이의 블로그 링크
- 인스타그램 링크
- 오시는 길 링크

---

## 디자인 요구사항

### 스타일
- **모던하고 깔끔한 디자인**: 최신 트렌드를 반영한 세련되고 심플한 UI
- **반응형 웹사이트**: 모바일, 태블릿, PC에서 모두 최적화된 반응형 디자인
- **부드러운 애니메이션**: 스크롤 시 자연스러운 섹션 이동 (스크롤 트리거 애니메이션)
- **자연스러운 색조합**: 각 섹션 구분 시 보기 편한 자연스러운 색조합 사용
- **시각적 효과**: 단순한 원색 대신 그라데이션, 그림자, 블러 등 매력적인 요소 활용
- **로딩 애니메이션**: 페이지 로드 시 자연스러운 로딩 효과 (스켈레톤 UI 추천)
- **Hover 효과**: 버튼이나 갤러리 카드에 마우스 오버 시 시각적인 피드백 제공

### 컬러 팔레트 제안
- 메인 컬러: 전문성과 신뢰를 주는 블루 계열
- 서브 컬러: 의료/제약 산업을 상징하는 화이트/그레이
- 액센트 컬러: 포인트를 주는 컬러 (예: 티얼 그린, 딥 블루)

### 타이포그래피
- 한글: 본고딕, Noto Sans KR 등 깔끔한 폰트
- 영문/숫자: Inter, Roboto 등 모던한 폰트
- 가독성을 위한 적절한 폰트 크기 및 행간

---

## 주요 기능

### 네비게이션
- **원페이지 스크롤**: 모든 섹션이 한 페이지에 연결되어 부드럽게 스크롤
- **네비게이션 바**: 
  - 각 섹션으로 이동할 수 있는 고정 네비게이션 바
  - 스크롤 시 네비게이션 바 스타일 변경 (투명 → 불투명)
  - 현재 섹션 하이라이트
  - 모바일: 햄버거 메뉴
  - 섹션 순서와 네비게이션 메뉴 순서 동일하게 구성

### 반응형 브레이크포인트
- 모바일: 320px ~ 768px
- 태블릿: 769px ~ 1024px
- 데스크톱: 1025px 이상

---

## 관리자 시스템

### 접근
- 관리자 페이지 접근 URL: `/innokadm/`
- 로그인 화면 및 인증 시스템
- 세션 관리 및 보안 (CSRF 토큰 등)

### 관리자 기능

#### 1. 데이터 관리 (JSON 기반)
다음 섹션의 데이터를 JSON 형식으로 관리:
- 사업소개 (특화사업/일반사업/교육사업/규제전문 에이전시/브랜딩 지원 사업(M&A))
- 회사소개
- 고객센터 정보

**기능**:
- 데이터 추가, 수정, 삭제
- JSON 형식으로 다운로드
- JSON 형식으로 업로드
- 실시간 미리보기

#### 2. 게시판 관리 (MySQL 연동)
- **공지사항**: 일반 게시판 형식
  - 조회, 입력, 수정, 삭제
  - 첨부파일 업로드 기능
  - 검색 기능
- **견적문의**: 질문답변 게시판
  - 조회, 입력, 수정, 삭제
  - 비밀번호 관리
  - 관리자 답변 기능
- **자주하는 질문**: 질문답변 게시판
  - 조회, 입력, 수정, 삭제
  - 비밀번호 관리
  - 질문/답변 관리
  - 답변일자 자동 기록

---

## 데이터 구조

### JSON 데이터 구조 예시

#### 사업소개 프로젝트 데이터 (projects.json)
```json
{
  "specialized": [
    {
      "id": 1,
      "title": "프로젝트 제목",
      "description": "프로젝트 설명",
      "image": "이미지 URL",
      "startDate": "2024-01-01",
      "endDate": "2024-12-31",
      "client": "고객사명"
    }
  ],
  "general": [],
  "education": [],
  "regulatory": [],
  "m&a": []
}
```

#### 회사소개 데이터 (about.json)
```json
{
  "companySlogan": "보건복지부, 식약처, 교육부 등...",
  "representativeImage": "대표 이미지 URL",
  "history": [],
  "organization": {}
}
```

#### 고객센터 데이터 (contact.json)
```json
{
  "businessHours": "평일 오전 10시 ~ 오후 5시",
  "phone": "02-756-7094",
  "mobile": "010-7131-7094",
  "fax": "0504-207-7094",
  "email": "innogi2020@innok.kr",
  "address": "장우빌딩 서울특별시 용산구 후암동 339-4, 630호",
  "instagram": "https://www.instagram.com/innok_corporation/",
  "blog": "https://blog.naver.com/iosis1218"
}
```

### MySQL 데이터베이스 구조

#### 공지사항 테이블 (notices)
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- title (VARCHAR(255))
- author (VARCHAR(100))
- content (TEXT)
- views (INT, DEFAULT 0)
- created_at (DATETIME)
- updated_at (DATETIME)
- attachment (VARCHAR(255), NULL)
```

#### 견적문의 테이블 (estimates)
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- title (VARCHAR(255))
- author (VARCHAR(100))
- password (VARCHAR(255))
- content (TEXT)
- views (INT, DEFAULT 0)
- created_at (DATETIME)
- updated_at (DATETIME)
- answer (TEXT, NULL)
- answered_at (DATETIME, NULL)
```

#### FAQ 테이블 (faqs)
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- title (VARCHAR(255))
- author (VARCHAR(100))
- password (VARCHAR(255))
- question (TEXT)
- answer (TEXT, NULL)
- views (INT, DEFAULT 0)
- created_at (DATETIME)
- updated_at (DATETIME)
- answered_at (DATETIME, NULL)
```

#### 관리자 테이블 (admins)
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- username (VARCHAR(100), UNIQUE)
- password (VARCHAR(255))
- created_at (DATETIME)
- last_login (DATETIME, NULL)
```

---

## 기술 스택

### Frontend
- **HTML5**: 시맨틱 마크업
- **CSS3**: 
  - Flexbox/Grid 레이아웃
  - CSS Variables
  - 애니메이션 (CSS Transitions/Animations)
- **JavaScript (ES6+)**:
  - 바닐라 JavaScript 또는 프레임워크
  - 스크롤 애니메이션 라이브러리 (AOS, GSAP 등)
  - 모달/팝업 관리
- **Bootstrap 5**: 반응형 그리드 및 컴포넌트
- **추가 라이브러리 제안**:
  - jQuery (선택적)
  - Swiper.js (이미지 슬라이더)
  - Lightbox (갤러리)
  - Animate.css 또는 AOS (애니메이션)

### Backend
- **Django Framework**:
  - Django 4.x 또는 최신 버전
  - Django Admin 커스터마이징
  - REST API 구성 (DRF 선택적)
- **데이터베이스**:
  - MySQL 8.0
  - Django ORM 활용
- **인증 및 보안**:
  - Django Authentication
  - 비밀번호 해싱 (bcrypt)
  - CSRF 보호
  - XSS 방지

### 배포
- **GitHub Actions**: 
  - 자동 빌드 워크플로우 구성
  - GitHub Pages 배포
  - 시크릿 관리 (DATABASE_URL, SECRET_KEY 등)
- **정적 파일 호스팅**:
  - GitHub Pages (무료)
  - 또는 Netlify, Vercel (추가 옵션)

### 개발 환경
- **로컬 개발**:
  - Python 가상환경
  - MySQL 로컬 서버
  - 개발 서버 (Django runserver)
- **버전 관리**:
  - Git
  - GitHub

---

## 추가 고려사항

### 보안
- SQL Injection 방지 (Django ORM 사용)
- XSS 방지 (이스케이프 처리)
- CSRF 토큰 사용
- 비밀번호 암호화 저장
- 관리자 페이지 접근 제한 (IP 화이트리스트 선택적)
- 세션 타임아웃 설정
- HTTPS 적용 (프로덕션)

### 성능 최적화
- 이미지 최적화 (WebP 형식, 레이지 로딩)
- CSS/JS 파일 압축 및 미니파이
- CDN 활용 (정적 파일)
- 데이터베이스 인덱싱
- 캐싱 전략 (Django 캐시 프레임워크)

### SEO (검색 엔진 최적화)
- 메타 태그 (title, description, keywords)
- Open Graph 태그 (SNS 공유)
- 시맨틱 HTML 구조
- 구조화된 데이터 (JSON-LD)
- 사이트맵 (sitemap.xml)
- robots.txt

### 접근성 (a11y)
- ARIA 레이블
- 키보드 네비게이션 지원
- 스크린 리더 호환
- 색상 대비율 준수 (WCAG 2.1)
- 이미지 alt 텍스트

### 브라우저 호환성
- Chrome, Firefox, Safari, Edge 최신 버전 지원
- 모바일 브라우저 (iOS Safari, Chrome Mobile) 지원

### 추가 기능 제안
- **다국어 지원**: 한국어/영어 (선택적)
- **프린트 스타일**: 인쇄 시 최적화된 스타일
- **다크 모드**: 사용자 선택 가능한 다크 모드 (선택적)
- **뉴스레터 구독**: 이메일 수집 및 구독 기능 (선택적)
- **실시간 채팅**: 고객 상담 챗봇 연동 (선택적)
- **Google Analytics**: 방문자 분석
- **Google Search Console**: SEO 관리

---

## 개발 단계 제안

### Phase 1: 기획 및 설계
1. 와이어프레임 작성
2. 디자인 목업 작성
3. 데이터베이스 스키마 설계
4. API 설계

### Phase 2: 개발
1. 환경 설정 (가상환경, 데이터베이스)
2. Django 프로젝트 초기화
3. 모델 생성 및 마이그레이션
4. 관리자 페이지 개발
5. 프론트엔드 레이아웃 구성
6. 각 섹션 구현
7. 반응형 디자인 적용
8. 애니메이션 및 인터랙션 추가

### Phase 3: 테스트
1. 기능 테스트
2. 반응형 테스트
3. 브라우저 호환성 테스트
4. 보안 테스트
5. 성능 테스트

### Phase 4: 배포
1. GitHub Actions 워크플로우 구성
2. 프로덕션 환경 설정
3. 배포 및 검증

---

## 참고사항
- 모든 이미지는 적절한 크기로 최적화
- 외부 링크는 새 탭에서 열리도록 설정 (target="_blank")
- 로딩 시간 최소화
- 사용자 경험(UX) 우선 고려
- 모바일 퍼스트 접근 방식 권장

---

이 프롬프트를 웹 제작 AI 서비스에 입력하여 프로젝트를 진행하세요.


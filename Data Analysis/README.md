# Data Analysis(데이터 전 처리)

---

[TOC]

---



## Intro
> 공공데이터 포털에서 제공하는 캠핑장 데이터는 정보 부족으로 태그화 진행이 어려움
> -> 크롤링을 통해 데이터를 추가했음
![데이터 전 처리 csv](https://user-images.githubusercontent.com/62299120/113971377-a01f5100-9873-11eb-8fe6-35a65c63428a.PNG)

### Crawling
- 네이버 지도에서 야영장명 검색하여 주소 확인 후 맞는 야영장 블로그 링크 10개의 내용을 긁어온다.
- 블로그 내용을 명사 카운터화 하여 태그화 하는 방법은 긍정적인 문장과 부정적인 문장을 판단하지 않아 태그 신뢰성에 문제가 있음
- -> 신뢰성을 올리기 위해 딥 러닝을 통해 자연어 처리 (긍/부정 판단 분석)를 진행하여  긍정 문장만을 태그화 진행

### NLP(자연어 처리)

- 긍정/부정 문장 판단 가능하게끔 학습이 필요
- 학습 데이터는 영화리뷰 댓글 긍/부정으로 나눈 데이터를 사용
![영화 리뷰 긍정 부정 점수](https://user-images.githubusercontent.com/62299120/113970760-6437bc00-9872-11eb-9e0f-5a86952f1e17.PNG)
- -> 긍/부정 단어(ex> 아니,싫어,별로다,긍정적,인상적)인 단어로 판단하기 때문에 학습 데이터론 상관없다고 판단
- - 문장 토큰화 실행하여 단어만 살림
- tensorflow의 Sequential모델을 사용
- -> 하나의 입력 텐서와 출력 텐서가 있는 일반적인 레이어이기 때문(긍정/부정 점수가 있어 정형적인 데이터)
- 학습 정확성 및 결과
![학습 결과 정확률](https://user-images.githubusercontent.com/62299120/113970733-55e9a000-9872-11eb-81e3-0ad4980b2092.PNG)
![감정분석 결과](https://user-images.githubusercontent.com/62299120/113970850-96e1b480-9872-11eb-9b6e-38b36b8af096.PNG)
- 정확성 85%이며 캠핑장 블로그 리뷰에 대해서도 긍/부정 판단이 잘됨
- 블로그 리뷰는 해쉬태그와 문장으로 구성됨
- 해쉬태그 : 긍/부정 판단 x -> 입지 구분 단어만 판단하여 태그 토큰 카운터
- 문장 : 긍/부정 판단 O -> 긍정문장에 대해서만 명사만 토큰화하여 입지 구분 단어와 유사한 단어를 입지 구분 단어 판단하여 태그 토큰 카운터 
- 입지구분 리스트와 해쉬태그 및 긍정문장 토큰화 
![입지구분 리스트](https://user-images.githubusercontent.com/62299120/113970973-d1e3e800-9872-11eb-952b-914b1d0d8306.PNG)
![해쉬태그는 따로 생각 편집](https://user-images.githubusercontent.com/62299120/113971295-79611a80-9873-11eb-81b1-f4c0db7f57f2.png)
![입지구분 결과](https://user-images.githubusercontent.com/62299120/113971325-867e0980-9873-11eb-97e3-6a2b51383a63.PNG)

- 데이터 추가한 데이터 셋
![데이터 전 처리 후 csv](https://user-images.githubusercontent.com/62299120/113971372-9eee2400-9873-11eb-838e-73bde0bd36d3.PNG)

## 서비스 소개

> `캠퍼스` 플랫폼에서는 크게 **캠핑장 추천 , 검색**의 2가지 세부서비스를 제공한다.
>
> - In this platform, users can utilize 2 services of `recommend`, `Search`

**Main Page**

- 메인 페이지로는 **추천태그별 캠핑장 리스트**가 띄워지게 된다.

![](Docs/img/MainPage.gif)

- 로그인과 회원가입을 을 통해 개인별 추천서비스를 받을 수 있고, 좋아요와 댓글을 남길 수 있다.




![](Docs/img/login.png)





![](Docs/img/register.png)



- 캠핑장 클릭시 Detail UI


![](Docs/img/DetailPage.gif)





### 1. 키워드 검색

- 태그가 아닌 일반검색으로 검색하면 해당 검색어를 포함된(이름또는 지역) 캠핑장 리스트가 출력된다.

![](Docs/img/SearchWord.gif)



### 2. 태그로 검색

- 태그로 검색하게 되면, 캠핑장의 태그가 해당태그인 리스트를 출력 한다.

![](Docs/img/SearchTag.gif)




## 설치 안내

> `git clone`을 한 후 아래의 작업을 진행해야 프론트 서버를 실행할 수 있다.

**1단계: npm 설치**

- `frontend` 프로젝트 폴더에서 npm을 설치한다.

```bash
npm install
npm run serve
```

**2단계: 환경변수 설정**

- `frontend` 폴더 내의 최상위 창에서 환경변수 `.env.local`이라는 파일을 생성한다.

- 환경변수로 관리하는 데이터는 다음과 같다.

  ```markdown
  ## .env.local
  
  VUE_APP_SERVER_URL=<서버 URL>
  VUE_APP_MAP_API_KEY=<카카오 지도 API Javascript 키>
  VUE_APP_SERVER_URL_C=<크롤링 서버 URL>
  ```
  
- `backend` 프로젝트 폴더에서 모듈을 설치한다.
```bash
pip install -r requirements.txt
python manage.py runserver
```

> 


## File Manifest

>**Naming Rule**
>
>- 파일 명은 `PascalCase`를 따른다.
>- 변수 및 함수명은 `snake_case`를 따른다.

### Frontend

- 폴더 구조는 `member`, `app`, `campsite`로 구분한다.

  ```markdown
  1. member
  - 회원계정 관련
  2. app
  - 메인페이지
  3. campsite
  - 캠핑장 추천 서비스 관련

### Backend


 -폴더구조는 서버 `Back-end`, 앱 단위 `main`, `camp`로 구분된다.
 
    
    1. DB 연동
    - python manage.py inspectdb (db 감지 및 model.py 코드 작성 용이)
        
    2.DB가 변경 되었을 시
    - python manage.py makemigrations
    - python manage.py migrate



### Database

### ERdiagram
![](Docs/img/erd.png)



## 저작권 및 사용권 정보

- 캠핑장 추천에서 사용되는 캠핑장 정보는 한국관광공사에서 제공하는 [캠핑장 정보 API]( http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList)를 활용하였다.


```markdown
- axios
- lodash
- vue bootstrap-vue bootstrap
- less less-loader
- mint-ui -S
- vue-awesome-swiper
- vuex
```



## 해결한 버그

> 코드를 서버에 올렸을 때 발생하는 주요 버그 및 그에 대한 해결법을 정리하였다.

**:Aws에 띄운 mysql과 Django가 연결되지 않는다.**

**원인**

- 계정에 대한 권한문제

**해결방안**

- 계정을 새로 생성하고, 해당 스키마에 대한 권한을 부여하여 해결했다.



## 알려진 버그

> 아직 없습니다.



## 배포


> https://j4a304.p.ssafy.io







***Copyright* © 2021 SSAFY_SEOUL3_TEAM4_캠퍼스**


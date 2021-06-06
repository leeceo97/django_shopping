# 쇼핑몰 (Django, DjangorestFramework)

### ✏ Description

- (세션을 이용한)유저의 회원가입, 로그인 기능
- 상품(목록, 생성, 상세보기)
- 주문(조회, 생성)
- class형 뷰의 사용, api 생성및 활용
- 유저별 ADMIN,USER두가지 권한 부여
- 배포(GCP) url: 

### Model Composition

```python
User {
	id: number;        // 숫자, 자동 생성
	email: string;     // 문자열(이메일 형식), 필수값
  password: string;  // 문자열, 필수값
  level: choices;    // 문자열(선택)
  created_at: date;  // 날짜형, 생성된 시간(자동 생성)
}

Board {
    id: number;        // 숫자, 자동 생성
    contents: string;   //문자열, 필수값, 게시판 내용
    title: string;    // 문자열, 필수값, 게시판 제목
    writer:; // 외래키, 'accounts.User', 게시판 작성자
    tags:; // 외래키, 'tag.Taf', 게시글 태그
    created_at: date; //날짜형, 생성된 시간(자동 생성)
    updated_at: date; //날짜형, 수정된 시간(자동 생성)
}

Order{
    id: number;     //숫자, 자동생성
    user:;      //외래키, 주문자
    product:;    //외래키, 주문 상품
    quantity: integer;   //숫자, 주문 수량
    created_at: date; //날짜형, 생성된 시간(자동 생성)
}

Product{
    id: number; //숫자, 자동생성
    name:string; //문자열, 상품명
    price:integer; //숫자, 가격
    description: string; //문자열, 상품설명
    stuck: integer; //숫자, 재고수량
    created_at: date; //날짜형, 생성된 시간(자동생성) 
}

```

### ⚙ Envirionments (python 3.8.0)

> pip install django==3.1.7
> pip install djangorestframework

❗ And, you have to create `.env` file in root.

```
Project tree
------------
root
├── venv
├── README.md
├── shopping
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── accounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    ├── decorators.py
    └── views.py
└── product
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── orders
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br>



### ▶ Execution

> pip install httpie

```python
python manage.py makemigrations

python manage.py migrate

# execute django web server
python manage.py runserver

# if you see error "No such table Todo",
## python manage.py makemigrations todo
## python manage.py migrate
## python manage.py runserver

""" in another cmd """
# please user httpie for test

```

<br>


### ▶ 후기
장고의 클래스형뷰와 일부기능을 api를 사용해서 프론트엔드 단에서
받아 사용하는 개인프로젝트를 만들어 보았는데, 확실히 코드가 간결해지고
구현을 빠르게 사용하는데 좋다는 느낌을 받았다. 일부기능을 api로 구현했는데
api로 구현을 할시 다른부분보다 view가 가장큰 혜택을 받는다고 느꼈다. 원래
클래스형뷰를 사용해 프로젝트를 만들어봤는데 이번기회를 통해 클래스형뷰의 
장점을 다시한번 제대로 느낄수 있었고 얼마든지 리팩토링을 통해 코드가 
발전시킬수 있다는 생각을 하게 되었다. 이레포지토리는 계속해서 발전시킬 생각이며
최종적으로는 drf를 통해 프론트와 백엔드를 완전히 분리시키는 작업으로 종결될것
같다는 생각을했다!!

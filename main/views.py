from django.shortcuts import render, redirect

# Create your views here.

def mainpage(request):
    context = {
        'name' : '최선우',
        'generation': 13,
        'contentLessons':[
        'template (html, view, url)',
        'template 언어',
        '효율적 코드 (template 상속, navbar 분리)',
        'static (css, image)'
        ],
        'week' : 2,
        'info': {'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'},
        'lessons' : [
        '사용자요청-함수-모델(데이터베이스)-함수-인터페이스-사용자',
        'gitignore의 기능: 파일들이 git에서 충돌나지 않게 해줌',
        'templates 폴더: html, css를 모아서 관리 (앱 이름으로 한번 더 폴더를 묶어서 헷갈리지 않게 함)',
        'main>templates>main>mainpage.html (ctrl+k+f로 정렬)'],
        
        'lessons1' : [
            '1. views.py를 통해 mainpage가 렌더링 될 수 있게 함 (함수를 통해)',
        'def 함수이름(request):return render(request, \'폴더/파일.html\')',
        '*렌더링=웹페이지에서 HTML, CSS, JS 같은 코드들을 실제로 브라우저 화면에 표시하는 것',
        '2. urls.py를 통해 main앱에서 view 함수 불러옴',
        '3. bash에서 python manage.py runserver 명령어+ctrl 클릭으로 연결 확인'],
        
        'lessons2':[
        '1. html의 nav에 #으로 되어 있는 부분을 {% url \'이름\'%} 형식으로 변경',
        'urls.py에서 지정한 이름을 활용해 html 페이지에서 해당 페이지로 이동할 수 있도록 링크 걸어줌',
        '2. view에서 생성한 데이터를 html에서 {{ 변수명 }} 형식을 통해 사용 가능',
        '{% 반복문 %} or {% 조건문 %} 형태로도 사용 가능',
        'ex) 함수에서 context 내에 작성한 \'generation\' : 13, {{ generation }}기=13기',
        '* {{변수명 | 필터 }}로 템플릿 변수를 특정 서식에 따라 변환',
        '* {# 주석처리 내용 #}',],
        
        'lessons3' : [
        '1. 반복되는 코드를 분리해서 project 폴더 - templates 폴더 - base.html 파일에 넣기',
        '2. 페이지.html에 ',
        '{% extends \'base.html\' %}',
        '{% block content %}',
        '내용',
        '{% endblock %}',
        '앞과 뒤에 추가',
        '3. 연결 확인하면 오류->settings.py에서 import os하고 DIRS에 templates 추가',
        '4. templates 폴더-shared 폴더-_navbar.html 파일에 base.html에 포함된 nav 영역 옮기기',
        '5. 분리한 _navbar.html을 base.html에 상속 시킴'
        ],

    }
    
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')
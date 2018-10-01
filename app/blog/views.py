from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
        # 'titles': titles
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    # templates/blog/post_detail.html
    # post가 가진 title, text, author, created_date, published_date를 적절히 출력
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    """
    template: blog/post_create.html
    URL :     /posts/create/

    1. 템플릿 하나의 <form>요소를 구현
        input[name="title"]
        textarea[name="text"]
        button[type="submit"]

    2. post_create.html을 보여주는 링크를 base.html에 구현
        {% url %} 태그를 사용할 것

    :param request:
    :return:
    """
    if request.method == 'POST':
        #POST요청이 왔을 경우
        # 새 글을 작성하고 원하는 페이지로 돌아가도록 함

        # 데이터는 request.POST안에 있음
        #HttpResponse를 돌려줌
        # 제목: <제목데이터><br>내용: <내용데이터>
        # 위 문자열을 가지고 response 돌려주기
        title = request.POST['title']
        text = request.POST['text']

        # objects.create() 메서드를 사용해서
        # 새 Post객체를 생성하며 DB에 저장 (create() 실행의 반환값은 'post'변수에 할당)
        # title, text 는 request.POST에서 가져온 내용
        # author는 request.user
        # 리턴하는 결과는 같은 문자열이지만,
        # 문자열을 생성할 때 만들어진 Post객체('post'변수)의 title 속성, text속성을 사용
        post = Post.objects.create(
            author=request.user,
            title=title,
            text=text,
        )
        #  글 목록 페이지로 Redirect 응답을 보냄
        # next_path = reverse('post-list')
        # return HttpResponseRedirect(next_path)

        # URL Name으로부터의 reverse과정이 추상화 되어있음
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html')

def post_update(request, pk):
    # URL
    # /posts/<pk>/update/

    #Template
    # blog/post_update.html

    #템플릿은 post_create.html의 내용과 같으나
    # input[name=title]과 textarea[name=text]의 내용을
    # 매개변수의 'pk'에 해당하는 Post의 title, text속성으로 미리 채운 상태로 form을 렌더링
    # -> context dict 에 'post'키에 해당하는 Post Instance를 담아서 보내 사용

    #post_detail view에서
    # 특정 pk의 Post를 가져와서 템플릿으로 전달
    # 템플릿에서 전달받은 특정 Post를 사용

    #post_create view에서
    # form형태 보기
    # input 속성의 기본값은 value
    # textarea속성의 기본값은 열림/닫힘 태그 사이의 텍스트
    post = Post.objects.get(id=pk)
    context= {
        'post': post,
    }
    return render(request, 'blog/post_update.html', context)
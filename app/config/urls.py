"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import blog
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', views.post_list, name='post-list'),

    # /posts/1/ <- 이 경우에 해당하는 정규표현식 패턴이
    # blog.views.post_detail <- 여기로 전달되도록 설정 및 뷰 함수 구현
    # -> 이 뷰는 'Post Detail'이라는 문자열을 HttpResponse를 사용해 리턴
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post-detail'),
    #request가 오면
    # post_detail(request = request, pk = <그룹부분에 주어진 값>
    url(r'^posts/create/$', views.post_create, name='post-create'),
    url(r'^posts/(?P<pk>\d+)/update/$', views.post_update, name='post-update'),
]

from django.http import HttpResponse
from django.utils import timezone


def post_list(request):
    #현재 지역에 맞는 날짜&시간 객체 할당
    current_time = timezone.now()
    '''

    :param request:실제 HTTP요청에 대한 정보를 가진 객체
    :return:
    '''
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            #날짜 & 시간 객체가 가진 정보를 문자열로 변환
            current_time.strftime('%Y, %m, %d<br>%H:%M:%S')
        )
    )
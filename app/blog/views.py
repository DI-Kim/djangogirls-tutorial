from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_date')

    content = ''
    content += '<ul>'
    for post in posts:
        content += f'<li>{post.title}</li>'
    content += '</ul>'

    context = {
        'posts': posts,
        # 'titles': titles
    }
    return render(request, 'blog/post_list.html', context)
from django.shortcuts import render, redirect, HttpResponse

# import comment model
from .models import Comment, Blog

def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    try:
        get_post = Blog.objects.get(pk=id)
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            website = request.POST.get('website')
            message = request.POST.get('message')

            comment_add = Comment.objects.create(post=get_post, name=name, email=email, website=website, message=message)
            comment_add.save()
            return redirect(url)

    except Exception as e:
        return HttpResponse("<a href='/'>Home</a>")
    return HttpResponse('workign')
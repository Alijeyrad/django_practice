from django.shortcuts import render, get_object_or_404
from home.models import Post
import datetime

# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status = 1).filter(published_date__lte=datetime.datetime.now())
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = Post.objects.filter(status=1)
    post = get_object_or_404(post, id=pid)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)
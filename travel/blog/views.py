from django.shortcuts import render, get_object_or_404
from home.models import Post
import datetime

# My functions

# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status = 1).filter(published_date__lte=datetime.datetime.now())
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    all_posts = Post.objects.filter(status=1).order_by('id')
    post = get_object_or_404(all_posts, id=pid)
    post_index = list(all_posts).index(post)
    try:
        next_post = [list(all_posts)[post_index+1]]
    except:
        next_post = []
    try:
        prev_post = [list(all_posts)[post_index-1]]
    except:
        prev_post = []
    context = {
        'post':post,
        'next_post':False if len(next_post) == 0 else next_post[0],
        'prev_post':False if len(prev_post) == 0 else prev_post[0]
    }
    return render(request, 'blog/blog-single.html', context)
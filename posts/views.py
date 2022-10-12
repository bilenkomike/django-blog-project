from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Post
from stories.models import Story
from comments.models import Comment






def index(request):

    posts = Post.objects.order_by('-date')
    stories = Story.objects.order_by('-id')[:4]
    paginator = Paginator(posts, 2)


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    
    
    context = {
        'posts': page_obj,
        'stories' : stories
    }
    return render(request, 'posts/index.html', context)

def add_post(request):
    if request.method == 'POST':
        if request.POST.get('post-text') and request.FILES.get('image'):
            post = Post(description=request.POST.get('post-text'), photo_main=request.FILES.get('image'))
        elif request.POST.get('post-text') and not request.FILES.get('image'):
            post = Post(description=request.POST.get('post-text'))
        post.save()
        return redirect('index')

    else: 
        return redirect('index')


def about(request):
    return render(request, 'posts/about.html')

    

def advertisement(request):
    return render(request, 'posts/advertisement.html')


def post(request, pk):
    # pk = inputed number
    post = Post.objects.get(id=pk)
    Post.objects.filter(id=pk).update(views=post.views + 1)
    posts = Post.objects.order_by('-views')[:4]
    comments = Comment.objects.filter(post=post).order_by('-id')
    context = {
        'post':post,
        'relateds': posts,
        'comments': comments
    }


    return render(request, 'posts/post.html', context)



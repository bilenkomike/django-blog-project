from django.shortcuts import render, redirect
from posts.models import Post


# Create your views here.
def search(request):
    search = request.GET.get('search')
    print(search)
    if search == '':
        return redirect('index')

    results = Post.objects.order_by('-id').filter(title__icontains=search )
    results2 = Post.objects.order_by('-id').filter(description__icontains=search)
    context = {
        'results':results,
        'results2':results2,
        'search': search
    }
    return render(request, 'search/search.html', context)
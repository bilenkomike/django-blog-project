from django.shortcuts import render
from .models import Work

from django.core.paginator import Paginator

# Create your views here.


def works(request):
    works = Work.objects.order_by('-id')
    paginator = Paginator(works, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'works': page_obj
    }

    return render(request, 'works/works.html', context)
    


def work(request, pk):
    work  = Work.objects.get(id=pk)
    Work.objects.filter(id=pk).update(views=work.views + 1)
    context = {
        'work':work
    }
    
    return render(request, 'works/work.html', context)
from django.shortcuts import redirect
from .models import Contact
from accounts.models import Account

# Create your views here.
def contact(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('fullname') and request.POST.get('message') and request.POST.get('user_id') != '0':
            account = Account.objects.get(pk = request.POST.get('user_id'))
            contact = Contact(email=request.POST.get('email'), fullname=request.POST.get('fullname'), message=request.POST.get('message'), user=account)
            contact.save()
        elif request.POST.get('email') and request.POST.get('fullname') and request.POST.get('message') and request.POST.get('user_id') == '0':
            contact = Contact(email=request.POST.get('email'), fullname=request.POST.get('fullname'), message=request.POST.get('message'))
            contact.save()
        else: 
            raise Exception('Invalid data input')
        return redirect('index')
    else:
        return redirect('index')
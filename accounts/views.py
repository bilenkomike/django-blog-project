from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import Account

# Create your views here.
import os


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password_again']

        if password == password_again:
            if User.objects.filter(email=email).exists():
                raise Exception('This user exists')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,email=email)
                
                user.save()

                account = Account(user=user, phone=phone)
                account.save()
                auth.login(request, user)
                return redirect('index')
                
        else:
            raise Exception('The passwords not equal')
    else: 
        return render(request, 'accounts/signup.html')
    
    # return render(request, 'accounts/signup.html')



def signin(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return redirect('signin')
    else:

        return render(request, 'accounts/signin.html')




def profile(request):
    if request.method == 'GET':
        account = Account.objects.get(user=request.user)
        context = {
            'account':account
        }
        return render(request, 'accounts/profile.html', context)
    elif request.method == 'POST':
        user = User.objects.filter(id=request.user.id)
        account = Account.objects.get(user=request.user)
        print(account)
        
        

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        # password = request.POST['password']
        # password_again = request.POST['password_again']

        # avatar = request.FILES.get('avatar')
        

        


        if len(request.FILES) > 0:
            if len(account.photo) > 0:
                os.remove(account.photo.path)
            account.photo = request.FILES['avatar']
            account.phone = request.POST.get('phone')
            account.save()
        else:
            account.phone = phone
            account.save()
        

        # if password and password_again:
        #     if password != password_again:
        #         raise Exception('Passwords not equal')
        #     else:
        #         user.update(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        #         print(user)
        #         user = user.authenticate(username=username, password=password)
        #         auth.login(request,user)
                
        # else:
        user.update(username=username, first_name=first_name, last_name=last_name, email=email)
        
        # account.update(phone=phone)

            
        return redirect('profile')

def logout(request):
    if request.method == 'POST':

        auth.logout(request)
        return redirect('index')
    return redirect('index')
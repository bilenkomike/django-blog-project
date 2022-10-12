from django.shortcuts import redirect
from django.contrib.auth.models import User
from accounts.models import Account
from .models import Comment
from posts.models import Post

# Create your views here.
def add_comment(request):
    if request.method == 'POST':
        
        if request.POST.get('comment-text'):
            account = Account.objects.get(user=request.POST.get('user'))
            post = Post.objects.get(pk=request.POST.get('post'))
            comment = Comment(comment=request.POST.get('comment-text'), user=account, post=post)
            
            try:
                comment.save()
            except:
                raise Exception('Error saving data! Verify data types')

        
        
        return redirect('/post/'+request.POST.get('post')+'/')
    else: 
        return redirect('index')
from django.shortcuts import render,redirect
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def home(request):
    data = Blog.objects.all() # SELECT * FROM `blog`
    context = {
        'blog':data
    }
    return render(request,'index.html',context)

def details(request):
    return render(request,'details.html')

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        u = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST['pass2']
        if pass1==pass2:
            u = User(username=u)
            u.set_password(pass1)
            u.save()
            return redirect('login')

        else:
            return redirect('signup')

def singnin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('pass1')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')


@login_required(login_url='login')
def dashbord(request):
    return render(request,'dashboard.html')
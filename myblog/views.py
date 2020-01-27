from django.shortcuts import render,redirect
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def signout(request):
    logout(request)
    return redirect('login')

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
            try:
                u.save()
                messages.add_message(request,messages.SUCCESS,"your account is created successfully")
                return redirect('login')
            except:
                messages.add_message(request,messages.ERROR,'user with this username already exist')
                return redirect('signup')

        else:
            messages.add_message(request,messages.ERROR,"username and password does not match")
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
            messages.add_message(request,messages.ERROR,'username or password does not match')
            return redirect('login')


@login_required(login_url='login')
def dashbord(request):
    return render(request,'dashboard.html')
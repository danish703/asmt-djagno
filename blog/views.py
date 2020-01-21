from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog
# Create your views here.

def remove(request,id):
    a = Blog.objects.get(pk=id)
    a.delete()
    return redirect('allnews')

def allnews(request):
    all = Blog.objects.all()
    context = {
        'news':all
    }
    return render(request,'all_news.html',context)

def edit(request,id):
    b = Blog.objects.get(pk=id)
    form = BlogForm(request.POST or None,instance=b)
    if form.is_valid():
        form.save()
        return redirect('allnews')

    context = {
        'form':form,
    }
    return render(request,'edit.html',context)

def create(request):
    if request.method=='GET':
        form = BlogForm()
        context = {
            'form':form
        }
        return render(request,'create_news.html',context)
    else:
        form = BlogForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'create_news.html',{'form':form})
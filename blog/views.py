from django.shortcuts import render,redirect
from .forms import BlogForm
# Create your views here.
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
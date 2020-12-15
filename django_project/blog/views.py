from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import CreateBlog

def home(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request,'blog/home.html',{'blogs':blogs})

def about(request):
    return render(request,'blog/about.html')

def blog_detail(request,slug):
    blog=Blog.objects.get(slug=slug)
    return render(request,'blog/blog_detail.html',{'blog':blog})

@login_required(login_url='/accounts/login/')
def blog_create(request):
    if request.method=='POST':
        form=CreateBlog(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('blog-home')
    else:
        form=CreateBlog()
    return render(request,'blog/blog_create.html',{'form':form})
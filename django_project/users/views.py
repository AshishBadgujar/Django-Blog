from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages


def signup_view(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            login(request,user)
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form=UserRegisterForm()
    return render(request,'users/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('blog-home')
    else:
        form=AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return render(request,'users/logout.html')

@login_required(login_url='/accounts/login/')
def profile_view(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated !')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)
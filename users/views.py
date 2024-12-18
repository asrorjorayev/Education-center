from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from  .froms import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegisterViev(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'users/register.html',context={"form":form})
    
    def post(self,request):
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Siz muvaffaqiyatli registratsiya qildingiz ")
            return redirect('index')

        return render(request,'users/register.html',context={"form":form})

class LoginViev(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login.html',context={"form":form})
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']
             user=authenticate(username=username,password=password)
             if user is not None:
                 login(request,user)
                 messages.success(request,"Siz muvaffaqiyatli login qildingiz ")
                 return redirect('index')
        return render(request,'users/login.html',context={"form":form})
    
class LogoutViev(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"Siz muvaffaqiyatli logout qildingiz ")
        return redirect('index')
    

class ProfileVievUpdate(LoginRequiredMixin,View):
    def get(self,request):
        form=ProfileUpdateViev(instance=request.user)
        return render(request,'users/update_profile.html',context={"form":form})

    def post(self,request):
        form=ProfileUpdateViev(instance=request.user,data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request,"Siz muvaffaqiyatli yangilanish qildingiz ")
            return redirect('users:profile')
        return render(request,'users/update_profile.html',context={"form":form})

class Profile_viev(LoginRequiredMixin,View):
    def get(self,request):

        return render(request,'users/profile_view.html')



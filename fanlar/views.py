from django.shortcuts import render,redirect,get_object_or_404
from fanlar.forms import RegisterCourseForm
from django.views import View
from django.contrib import messages
from .models import RegisterKurs,Fanlar

class RegisterCourseView(View):
    
    def get(self,request):
        form=RegisterCourseForm()
        return render(request,"course_register.html",context={"form":form})
    
    def post(self,request):
        form=RegisterCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Siz muvaffaqiyatli registratsiya qildingiz ")    
            return redirect("index")
        return render(request, "course_register.html", {"form": form}) 
 
     
def Categoriya_fan(request,id):
    categoriya=get_object_or_404(Fanlar,id=id)
    abtr=categoriya.fanlar.all()
    data={
        "abtr":abtr
        }
    return render(request,"categoriya.html",context=data)

 

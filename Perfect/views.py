from django.shortcuts import render,get_object_or_404
from fanlar.forms import RegisterCourseForm
from fanlar.models import RegisterKurs
def index(request):

    return render(request,'index.html')

def Qabuldagilar(request):
    royxat = RegisterKurs.objects.all()   # BU joyda royxatdan otganlarni hammasini olib beradi
    data = {
        "royhat": royxat
    }
    return render(request, "Royxatdan_otganlar.html", context=data)


 
    


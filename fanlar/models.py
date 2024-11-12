from django.db import models
from users.models import User

class Oquvchituvchilar(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()

    def __str__(self) :
        return self.name
        
class Fanlar(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='fanlar',null=True,blank=True)
    oqituvchi=models.ForeignKey(Oquvchituvchilar,on_delete=models.CASCADE,related_name="oqituvchi")

    def __str__(self) :
        return self.name

class Kunlar(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) :
        return self.name


class RegisterKurs(models.Model):
    ism=models.CharField(max_length=255)
    familya=models.CharField(max_length=55)
    phone=models.CharField(max_length=13,unique=True)
    kurs=models.ForeignKey(Fanlar,on_delete=models.CASCADE,)
    dars_kunlari=models.ForeignKey(Kunlar,on_delete=models.CASCADE)
    izoh=models.TextField()


    def __str__(self) -> str:
        return f"{self.familya}  {self.ism}"
    

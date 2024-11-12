from django.urls import path
from .views import *

app_name='fanlar'
urlpatterns=[
    path('course/',RegisterCourseView.as_view(),name="course"),
    path('categoriya_fan/',Categoriya_fan,name="categoriya_fan"),
]
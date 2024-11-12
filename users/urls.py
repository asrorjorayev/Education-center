from django.urls import path
from .views import *

app_name="users"
urlpatterns=[
    path("login/",LoginViev.as_view(),name="login_page"),
    path("register/",RegisterViev.as_view(),name="register"),
    path("logout/",LogoutViev.as_view(),name="logout_page"),
    path("update/",ProfileVievUpdate.as_view(),name="update"),
    path("profile/",Profile_viev.as_view(),name="profile"),
]
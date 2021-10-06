from django.urls import path
from user.views import *

app_name = "user"

urlpatterns = [
    path('signup',SignUp.as_view(),name="signup"),
    path('change_password', Change_password.as_view(), name="change_password"),
    path('sign',sign,name="sign"),
    path('profil',profil,name="profil"),
    path('logout', loguot_view, name='logout'),

]
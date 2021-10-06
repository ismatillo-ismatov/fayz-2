from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from user.form import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def sign(request):
    if request.method == "POST":
        login1 = request.POST['login']
        password = request.POST["password"]
        user = authenticate(request,username=login1,password=password)
        if user is not None:
            login(request,user)
            return redirect("enjoy:index")
    return render(request,"user/sign.html")
def post(reqeust):
    return render(reqeust,"user/sign.html")

class SignUp(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,"user/signup.html",{"form":form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"mafaqiyatli royhatdan otdingiz")
            return redirect("user:sign")
        else:
            return render(request,"user/signup.html",{"form":form})

@login_required(login_url='user:sign')
def profil(request):
    return render(request,"user/profil.html")

class Change_password(View):
    def get(self,request):
        return render(request,"user/change_password.html")
    def post(self,request):
        old_password = request.POST["old_password"]
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check = request.user.check_password(old_password)
        error = 0
        if not check:
            messages.add_message(request,messages.WARNING,"Avvalgi parol notorgi")
            error += 1
        elif password1 != password2:
            messages.add_message(request,messages.WARNING,"Parorlar mos emas")
            error += 1
        if error != 0:
            return render(request,"user/change_password.html")
        else:
            request.user.set_password(password1)
            return redirect('user:profil')

def loguot_view(request):
    logout(request)
    return redirect('enjoy:index')

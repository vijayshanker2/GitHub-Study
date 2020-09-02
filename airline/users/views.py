from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,"users/user.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( request, username = username, password = password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
            "message" : "The username and password do not match!!"
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
    "message":"You have successfully logged out."
    })

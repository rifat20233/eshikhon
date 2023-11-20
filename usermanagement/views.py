from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.

def login_page(request):
    if request.method =="GET":
        return render(request,'login.html')
    elif request.method =="POST":
        input_username = request.POST['username']
        input_password = request.POST['password']

        user = auth.authenticate(username=input_username,password=input_password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard_url')
        else:
            messages.error(request,"Username or password did not match")
            return render(request,'login.html')

def logout_session(request):
    auth.logout(request)
    return redirect('login_page')   
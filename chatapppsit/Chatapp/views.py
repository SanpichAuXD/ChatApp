from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def loginform(request):
    return render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')
def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def register(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']
    if password==repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username already exist")
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "This email already exists")
            return redirect('/signup')
        elif not username:
            messages.info(request, "Please enter username")
            return redirect('/signup')
        elif not email:
            messages.info(request, "Please enter email")
            return redirect('/signup')
        elif not password:
            messages.info(request, "Please enter password")
            return redirect('/signup')
        elif not repassword:
            messages.info(request, "Please enter repassword")
            return redirect('/signup')
        else:
            user = User.objects.create_user(
            username=username,
            password=password,
            email=email
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request, "Password not match") 
        return redirect('/signup')
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    #check username, password
    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/home')
    elif not username :
        messages.info(request, "Please enter username")
        return redirect('/')
    elif not password :
        messages.info(request, "Please enter password")
        return redirect('/')
    else :
        messages.info(request, "password is incorrect or there is no user with such name")
        return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect('/home')
    

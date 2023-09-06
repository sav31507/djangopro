from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    if request.method == 'POST':
        uname=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('/')
            else:
                user= User.objects.create_user(username=uname,email=email,password=password)
                user.save()

        else:
             messages.info(request,'passwd not match')
             return redirect('/')
        return redirect ('/')
    return render(request,'a.html')



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('pagere')
        else:
            messages.info(request,"invalid correction")
            return redirect('login')
    return render(request,'login.html')

def pagere(request):
    return HttpResponse('welcome')




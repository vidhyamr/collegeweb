from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth



def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already taken')
                return redirect('loginapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)


                user.save();
                print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('loginapp:login')
    return  render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('loginapp:student')
        else:
            messages.info(request, "invalid credentials")
        return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    return render(request,'form.html')
def about(request):
    return render(request,'aboutus.html')

def next(request):
    return render(request,'logout.html')

def student(request):
    return render(request,'student.html')




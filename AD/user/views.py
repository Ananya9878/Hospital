from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        username = request.POST.get("username")
        if password2 == password1:
            try:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.name = name
                user.save()
            except Exception as e:
                context = {'error':str(e)}
                return render(request,'user/signup.html',context=context)
        else:
            context = {'error':'Password Does not match'}
            return render(request,'user/signup.html',context=context)

        return redirect('../../../user/login')
    else:
        return render(request,"user/signup.html")

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password,request=request)
        if user is not None:
            login(request,user)
            return redirect('../../../hospital/')
        else:
            context = {'error':'Username or Password is not Valid'}
            return render(request,'user/login.html',context=context)

    else:
        return render(request,"user/login.html")


def log_out(request):
    logout(request)
    return redirect('../../../../../user/login')


def change_password(request):
    if request.method == 'POST':
        u = User.objects.get(username='username')
        u.set_password('new password')
        u.save()
        return HttpResponse('Working')








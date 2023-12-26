from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 

# username: deepkamalsingh
# password: 1


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is None:
            return render(request,'accounts/login.html',context={"error":"invalid username or password"})
        login(request, user) 
        return redirect('/admin')
    return render(request,'accounts/login.html',context={})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request,'accounts/logout.html',context={})


def register_view(request):
    return render(request,'accounts/login.html',context={})
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'error':"Username already exist"})
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'error':"Passsword are not same"})  

    return render(request,'register.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,"login.html", {"error": "Invalid username or password"})
    else:
        return render(request,'login.html')
    
def user_logout(request):
    logout(request)
    return redirect(request,'login')

@login_required

def dashboard(request):
    return render(request,'dashboard.html')
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'error':"Username already exist"})
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
            return render(request,'login.html')

        else:
            return render(request,'register.html',{'error':"Passsword are not same"})  
    else:
        return render(request,'login.html')
    

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                
                messages.info(request,'Username Already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                
                messages.info(request,'Email Already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                messages.info(request,'Username Created Sucessfully')
                return redirect('signin')
        else:
            
            messages.info(request,'Password Not Matching')
            return redirect('signup')
    else:
        return render(request,'signup_new.html')
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            
            return redirect(reverse('user')) 

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('signin')
        
    else:
        return render(request,'signin_new.html')





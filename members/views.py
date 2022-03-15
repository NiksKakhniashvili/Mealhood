from email import message
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
 

def home_page(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There Was An Error Logging In, Try Again...'))
            return redirect('login')



    else:
        context = {}
        return render(request,'authenticate/login.html',context)


def register(request):
    form = UserCreationForm()
    contexti = {
        'form':form
    }
    return render(request,"authenticate/register.html",contexti)
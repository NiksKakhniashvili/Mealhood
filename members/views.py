from email import message
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
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
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,"authenticate/register.html",{'form':form})

@login_required
def profile(request): 
    return render(request, 'authenticate/profile.html',{})
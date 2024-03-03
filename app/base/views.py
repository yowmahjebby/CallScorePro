from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        if request.POST.get('submit') == 'Login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

        elif request.POST.get('submit') == 'Register':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                pass

    return render(request, 'base/index.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def homePage(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def profilePage(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'base/profile.html', context)
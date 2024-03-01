from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not username or not password:
            messages.error(request, 'Please fill in both the username and password fields')
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect')

    context = {'page': 'login'}
    return render(request, 'base/login_registration.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_registration.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def profilePage(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'base/profile.html', context)
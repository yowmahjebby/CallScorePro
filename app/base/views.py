from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import RegisterUserForm
from .decorators import redirect_if_authenticated, allowed_users, superuser_only

# Create your views here.
@redirect_if_authenticated
def index(request):    
    if request.method == 'POST':
        if request.POST.get('submit') == 'Login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            
        elif request.POST.get('submit') == 'Register':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                group = Group.objects.get(name='Agent')
                user.groups.add(group)
                login(request, user)
                return redirect('home')
            else:
                pass

    return render(request, 'base/index.html')

@login_required(login_url='index')
def homePage(request):
    return render(request, 'base/home.html')

@login_required(login_url='index')
def profilePage(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'base/profile.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def billingPage(request):
    return render(request, 'base/billing.html')

def callsPage(request):
    return render(request, 'base/calls.html')

# @allowed_users(allowed_roles=['admin'])
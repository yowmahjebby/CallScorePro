from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.homePage, name='home'),
    path('profile/<str:username>', views.profilePage, name='profile'),
]
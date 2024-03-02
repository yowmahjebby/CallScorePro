from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.homePage, name='home'),
    path('profile/<str:username>', views.profilePage, name='profile'),
]
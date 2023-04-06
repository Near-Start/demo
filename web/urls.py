# _*_ coding: utf-8 _*_
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('node_search/', views.node_search, name='node_search'),
    path('answer/', views.answer, name='answer'),
    path('calGrade/', views.calGrade, name='calGrade'),
    path('showGrade/', views.showGrade, name='showGrade'),
    path('logout/', views.logout, name='logout'),
]

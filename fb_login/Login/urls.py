"""fb_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from Login.views import Register
from Login.views import resumeCreate,Register,viewresume,resumeEdit,resumeDelete,resumedetails,resumeview
urlpatterns = [
    path('resumeCreate/<int:pk>',resumeCreate,name='createresume'),
    path('Register',Register,name='Register'),
    path('resumeview/<int:pk>',resumeview,name='resumeview'),
    path("",lambda request:render(request,"resume/homebase.html")),
    path('resumeEdit/<int:pk>', resumeEdit, name='resumeEdit'),
    path('resumeDelete/<int:pk>',resumeDelete, name='resumeDelete'),
    path('viewresume',viewresume, name='viewresume'),
    path('resumedetails/<int:pk>',resumedetails,name='resumedetails'),
    path('Register',Register,name='Register'),
]

# -*- coding: utf-8 -*-

#from django.contrib import admin
from django.urls import path
from .views import signup_view
urlpatterns = [
    path('login/', signup_view ) ,
]

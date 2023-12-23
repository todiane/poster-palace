from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_pp, name='about'),

]

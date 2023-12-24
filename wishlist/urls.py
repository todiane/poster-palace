from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.wish_list, name='wish_list'),
    path('add_wish/', views.add_wish, name='add_wish'),
    path('delete_wish/',
         views.delete_wish, name='delete_wish'),
]

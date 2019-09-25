from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path('new/', views.addBook),
    path('after/', views.after),
    path('change/', views.change)
]
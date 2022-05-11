from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('literature/', views.literature),
    path('greeting/', views.greeting),
    path('registration/', views.registration_page),
    # path('authorization/', views.authorization_page)
]

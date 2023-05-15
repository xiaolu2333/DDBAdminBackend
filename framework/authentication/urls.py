from django.contrib import admin
from django.urls import path

from framework.authentication import views

api_version = 'v1'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('createUser/', views.create_user, name='create_user'),
]

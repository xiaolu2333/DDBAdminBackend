from django.contrib import admin
from django.urls import path

from framework.organizations import views

api_version = 'v1'

urlpatterns = [
    path('getOrganization/', views.get_organization, name='get_organization'),
    path('createOrganization', views.create_organization, name='create_organization'),
]

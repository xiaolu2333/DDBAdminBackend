from django.contrib import admin
from django.urls import path

from framework.organizations import views

api_version = 'v1'

urlpatterns = [
    path('getOrganizationList', views.get_organization_list, name='get_organization_list'),
    path('getOrganization/<int:id>', views.get_organization_detail, name='get_organization_detail'),
    path('createOrganization', views.create_organization, name='create_organization'),
    path('deleteOrganization/<int:id>', views.delete_organization, name='delete_organization'),
]

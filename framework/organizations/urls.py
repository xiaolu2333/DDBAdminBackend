from django.contrib import admin
from django.urls import path

from framework.organizations import views

api_version = 'v1'

urlpatterns = [
    path('getOrganizationList', views.get_organization_list, name='get_organization_list'),
    path('getOrganizationTree', views.get_organization_tree, name='get_organization_tree'),
    path('getOrganization', views.get_organization_detail, name='get_organization_detail'),
    path('createOrganization', views.create_organization, name='create_organization'),
    path('updateOrganization', views.update_organization, name='update_organization'),
    path('deleteOrganization', views.delete_organization, name='delete_organization'),
]

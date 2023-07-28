from django.contrib import admin
from django.urls import path

from framework.resources import views

api_version = 'v1'

urlpatterns = [
    path('getMenuList', views.get_menu_list, name='get_menu_list'),
    path('getMenu', views.get_menu_detail, name='get_menu_detail'),
    path('createMenu', views.create_menu, name='create_menu'),
    path('updateMenu', views.update_menu, name='update_menu'),
    path('deleteMenu', views.delete_menu, name='delete_menu'),
]

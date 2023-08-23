from django.urls import path

from framework.authentication import views

api_version = 'v1'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('createUser/', views.create_user, name='create_user'),

    path('createRole/', views.create_role, name='create_role'),
    path('updateRole/', views.update_role, name='update_role'),
    path('deleteRole/', views.delete_role, name='delete_role'),
    path('getRoleList/', views.get_role_list, name='get_role_list'),
    path('getRoleDetail/', views.get_role_detail, name='get_role_detail'),
]

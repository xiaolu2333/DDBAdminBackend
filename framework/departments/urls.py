from django.contrib import admin
from django.urls import path

from framework.departments import views

api_version = 'v1'

urlpatterns = [
    path('getDepartmentList', views.get_department_list, name='get_department_list'),
    path('getDepartment', views.get_department_detail, name='get_department_detail'),
    path('createDepartment', views.create_department, name='create_department'),
    path('updateDepartment', views.update_department, name='update_department'),
    path('deleteDepartment', views.delete_department, name='delete_department'),
]

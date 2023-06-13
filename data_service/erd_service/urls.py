from django.urls import path

from data_service.erd_service import views

api_version = 'v1'

urlpatterns = [
    # 获取ERD信息
    path('index', views.index, name='index'),
]

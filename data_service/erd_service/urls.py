from django.urls import path

from data_service.erd_service import views

api_version = 'v1'

urlpatterns = [
    # 获取ERD信息
    path('get_erd_data', views.get_erd_data, name='index'),
    # 获取树形结构数据
    path('get_tree_data', views.get_tree_data, name='get_tree_data'),
]

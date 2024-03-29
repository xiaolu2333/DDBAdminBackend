from django.urls import path

from data_management.data_tree_manage import views

api_version = 'v1'

urlpatterns = [
    path('index/', views.index, name='index'),

    # 获取树节点
    path('get_tree_node/', views.get_tree_node, name='get_tree_node'),

    # 创建树节点
    path('create_tree_node/', views.create_tree_node, name='create_tree_node'),

    # 获取数据类型
    path('get_data_type/', views.get_data_type, name='get_data_type'),
]

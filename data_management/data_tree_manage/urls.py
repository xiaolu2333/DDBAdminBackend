from django.urls import path

from data_management.data_tree_manage import views

api_version = 'v1'

urlpatterns = [
    path('index/', views.index, name='index'),

    # 创建树节点
    path('create_tree_node/', views.create_tree_node, name='create_tree_node')
]

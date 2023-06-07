from django.urls import path

from data_management.database_manage import views

api_version = 'v1'

urlpatterns = [
    # 获取数据库列表
    path('index/', views.index, name='index'),

    # 创建域内数据库
    path('create_domain_database/', views.create_domain_database, name='create_domain_database'),
    # 创建跨域数据库
    path('create_cross_domain_database/', views.create_cross_domain_database, name='create_cross_domain_database'),
    # 发布
    path('publish_database/', views.publish_database, name='publish_database')
]

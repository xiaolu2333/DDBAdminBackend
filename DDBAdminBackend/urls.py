"""DDBAdminBackend URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户、角色、权限管理
    path(
        'framework/authentication',
        include(('framework.authentication.urls', 'framework.authentication'), namespace='framework-authentication')
    ),

    # 组织机构管理
    path(
        'framework/organizations/',
        include(('framework.organizations.urls', 'framework.organizations'), namespace='framework-organizations')
    ),

    # 部门管理
    path(
        'framework/departments/',
        include(('framework.departments.urls', 'framework.departments'), namespace='framework-departments')
    ),

    # 学习测试应用
    path('test_app/', include(('test_app.urls', 'test_app'), namespace='test_app')),

    # 数据树管理
    path('data_management/data_tree_manage/',
         include(('data_management.data_tree_manage.urls', 'data_management.data_tree_manage'), namespace='data_tree_manage')),
]

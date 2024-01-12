"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: urls.py
 @DateTime: 2024/1/12 12:23
 @SoftWare: PyCharm
"""

from django.urls import path

from learn import views

urlpatterns = [
    ################################# element plus 相关 #################################
    # element plus 复选框传值
    path('element_plus/post_checkbox_data', views.post_checkbox_data, name='post_checkbox_data'),
    # element plus 复选框取值
    path('element_plus/get_checkbox_data', views.get_checkbox_data, name='get_checkbox_data'),


    ################################# vxetable 相关 #################################
    # 获取通用表格表头
    path('vxe_table/get_general_table_header', views.get_general_table_header, name='get_general_table_header'),
    # 获取通用表格数据
    path('vxe_table/get_general_table_data', views.get_general_table_data, name='get_general_table_data'),
]

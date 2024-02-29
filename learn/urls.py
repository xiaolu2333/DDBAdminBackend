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

    ################################# 前后端数据交互 #################################
    # 大文件分片上传
    path('data_interaction/upload_big_file_slice', views.upload_big_file_slice, name='upload_big_file'),
    # 合并大文件分片
    path('data_interaction/merge_big_file_slice', views.merge_big_file_slice, name='merge_big_file_slice'),

    ################################# http 请求相关 #################################
    # 重复请求
    path('http_request_response/test_repeat_request', views.test_repeat_request, name='test_repeat_request'),
]

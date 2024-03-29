from django.contrib import admin
from django.urls import path

from test_app import views

api_version = 'v1'

urlpatterns = [
    path('index', views.index, name='index'),
    path('vxe-table_handle_direct_update', views.handle_direct_update, name='direct_update'),
    path('vxe-table_handle_save_the_update', views.handle_save_the_update, name='save_the_update'),

    path('pagination_data', views.pagination_data, name='pagination_data'),
    path('scroll_pagination_data', views.scroll_pagination_data, name='scroll_pagination_data'),

    path('use_echarts_line_chart', views.use_echarts_line_chart, name='use_echarts_line_chart'),

    # 一般文件上传与下载
    path('upload_file', views.upload_file, name='upload_file'),
    path('download_file_by_stream', views.download_file_by_stream, name='download_file'),
    path('download_file_by_url', views.download_file_by_url, name='download_file_by_url'),
    # 表单文件上传与下载
    path('upload_form_file', views.upload_form_file, name='upload_form_file'),
    path('download_form_file', views.download_form_file, name='download_form_file'),
    # 文件断点续传
    path('upload_file_by_breakpoint', views.upload_file_by_breakpoint, name='upload_file_by_breakpoint'),
    # 文件分片上传
    path('upload_file_by_block', views.upload_file_by_block, name='upload_file_by_breakpoint'),
    # 中断文件上传
    path('interrupt_upload_request', views.interrupt_upload_request, name='interrupt_upload_request'),
    # 中断文件下载
    path('interrupt_download_request', views.interrupt_download_request, name='interrupt_download_request'),

    # visual数据可视化
    path('visual_data/aircraft_data', views.aircraft_data, name='aircraft_data'),

    # 前端埋点数据分析
    path('page_data_analysis', views.page_data_analysis, name='page_data_analysis'),
]

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
]

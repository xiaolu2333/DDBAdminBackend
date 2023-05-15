"""DDBAdminBackend URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'framework/',
        include(('framework.authentication.urls', 'framework.authentication'), namespace='framework-authentication')
    ),
    path('test_app/', include(('test_app.urls', 'test_app'), namespace='test_app')),
]

"""DDBAdminBackend URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'framework/authentication',
        include(('framework.authentication.urls', 'framework.authentication'), namespace='framework-authentication')
    ),
    path(
        'framework/organizations/',
        include(('framework.organizations.urls', 'framework.organizations'), namespace='framework-organizations')
    ),
    path(
        'framework/departments/',
        include(('framework.departments.urls', 'framework.departments'), namespace='framework-departments')
    ),

    path('test_app/', include(('test_app.urls', 'test_app'), namespace='test_app')),
]

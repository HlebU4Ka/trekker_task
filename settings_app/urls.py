"""
URL configuration for settings_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employee.views import busy_employees, important_tasks
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Tracking Tasks",
      default_version='v0.1',
      description="Tracking Tasks. Отслеживание задач и свободных сотрудников",
      terms_of_service="https://www.settings_app.com/terms/",
      contact=openapi.Contact(email="gelbkot57@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('busy_employees/', busy_employees, name='busy-employees'),
    path('important_tasks/', important_tasks, name='important-tasks'),
    path('api/', include('Employee.urls')),
    path('api/', include('Task.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]



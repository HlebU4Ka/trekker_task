from django.urls import path

from Task.views import TaskListCreateView, TaskDetailView
from settings_app.views import busy_employees, important_tasks
from .views import (
    EmployeeListCreateView, EmployeeDetailView,)


urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('busy-employees/', busy_employees, name='busy-employees'),
    path('important-tasks/', important_tasks, name='important-tasks'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

]
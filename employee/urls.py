from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, busy_employees, important_tasks

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('busy_employees/', busy_employees, name='busy-employees'),
    path('important_tasks/', important_tasks, name='important-tasks')
]
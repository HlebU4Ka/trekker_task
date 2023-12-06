from django.contrib import admin
from Employee.models import Employee
from Task.models import Task

admin.site.register(Employee)
admin.site.register(Task)
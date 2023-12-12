from django.contrib import admin
from Employee.models import Employee
from Task.models import Task


class EmployeeAdmin(admin.ModelAdmin):
    """
    Класс настроек административного интерфейса для модели Employee.
    """
    list_display = ('first_name', 'last_name', 'position')


class TaskAdmin(admin.ModelAdmin):
    """
    Класс настроек административного интерфейса для модели Task.
    """
    list_display = ('title', 'priority', 'executor', 'status')


# Регистрация моделей в административном интерфейсе Django
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)

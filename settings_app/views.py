from rest_framework.decorators import api_view
from rest_framework.response import Response
from Employee.models import Employee
from Task.models import Task
from settings_app.serializers import EmployeeSerializer, TaskSerializer


@api_view(['GET'])
def busy_employees(request):
    employees = Employee.objects.all()
    busy_employees = sorted(employees, key=lambda emp: emp.task_set.filter(status='active').count(), reverse=True)

    serialized_employees = EmployeeSerializer(busy_employees, many=True)
    return Response(serialized_employees.data)


@api_view(['GET'])
def important_tasks(request):
    # Получаем все важные задачи, от которых зависят другие задачи
    important_tasks = Task.objects.filter(priority='important', dependencies__isnull=False)

    result = []
    for task in important_tasks:
        # Находим сотрудников, которые могут взять такие задачи
        available_employees = Employee.objects.filter(
            task__isnull=True,  # Не имеют назначенных задач
            parent_task__isnull=True  # Не выполняют родительские задачи
        )

        # Отбираем сотрудников с наименьшей загрузкой
        available_employees = sorted(
            available_employees,
            key=lambda emp: emp.task_set.count(),
        )

        # Отбираем первого сотрудника с наименьшей загрузкой
        if available_employees:
            selected_employee = available_employees[0]
            result.append({
                'task': TaskSerializer(task).data,
                'employee': selected_employee.full_name,
            })

            # Назначаем задачу выбранному сотруднику
            task.executor = selected_employee
            task.save()

    return Response(result)
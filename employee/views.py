from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee
from task.models import Task
from employee.serializers import EmployeeSerializer, TaskSerializer
from rest_framework import generics


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def busy_employees(request):
    employees = Employee.objects.annotate(busy_tasks_count=models.Count('task', filter=models.Q(task__status='active')))
    busy_employees = sorted(employees, key=lambda emp: emp.busy_tasks_count, reverse=True)

    serialized_employees = EmployeeSerializer(busy_employees, many=True)
    return Response(serialized_employees.data)


@api_view(['GET'])
def important_tasks(request):
    important_tasks = Task.objects.filter(priority='important', dependencies__isnull=False).select_related('executor')

    result = []
    for task in important_tasks:
        available_employees = Employee.objects.filter(
            task__isnull=True,
            parent_task__isnull=True
        ).order_by('task__count')

        if available_employees:
            selected_employee = available_employees[0]
            result.append({
                'task': TaskSerializer(task).data,
                'employee': selected_employee.full_name,
            })

            task.executor = selected_employee
            task.save()

    return Response(result)
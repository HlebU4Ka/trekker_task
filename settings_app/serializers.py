from rest_framework import serializers
from Employee.models import Employee
from Task.models import Task


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['full_name', 'position']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'parent_task', 'executor', 'deadline', 'status']

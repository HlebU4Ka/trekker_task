from django.test import TestCase
from django.utils import timezone
from employee.models import Employee
from task.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(first_name='John', last_name='Doe', position='Developer')

    def test_task_creation(self):
        task = Task.objects.create(
            executor=self.employee,
            deadline=timezone.now() + timezone.timedelta(days=3),
            status='pending',
            priority='important',
            title='Finish project'
        )
        self.assertEqual(task.executor, self.employee)
        self.assertIsNotNone(task.deadline)
        self.assertEqual(task.status, 'pending')
        self.assertEqual(task.priority, 'important')
        self.assertEqual(task.title, 'Finish project')

    def test_task_creation_without_executor(self):
        task = Task.objects.create(
            deadline=timezone.now() + timezone.timedelta(days=3),
            status='pending',
            priority='normal',
            title='Finish project'
        )
        self.assertIsNone(task.executor)
        self.assertIsNotNone(task.deadline)
        self.assertEqual(task.status, 'pending')
        self.assertEqual(task.priority, 'normal')
        self.assertEqual(task.title, 'Finish project')

    def test_task_str_representation(self):
        task = Task.objects.create(
            executor=self.employee,
            deadline=timezone.now() + timezone.timedelta(days=5),
            status='in_progress',
            priority='normal',
            title='Review code'
        )
        self.assertEqual(str(task), 'Review code')

    def test_task_dependencies(self):
        parent_task = Task.objects.create(
            executor=self.employee,
            deadline=timezone.now() + timezone.timedelta(days=7),
            status='completed',
            priority='important',
            title='Parent task'
        )

        child_task = Task.objects.create(
            executor=self.employee,
            deadline=timezone.now() + timezone.timedelta(days=2),
            status='pending',
            priority='normal',
            title='Child task',
            parent_task=parent_task
        )

        self.assertEqual(parent_task.dependencies.count(), 1)
        self.assertEqual(parent_task.dependencies.first(), child_task)

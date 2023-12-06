# Generated by Django 4.2.8 on 2023-12-06 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_remove_employee_full_name_employee_first_name_and_more'),
        ('Task', '0002_employee_rename_title_task_name_task_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.employee'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
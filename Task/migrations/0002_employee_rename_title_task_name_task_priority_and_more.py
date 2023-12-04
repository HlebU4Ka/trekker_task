# Generated by Django 4.2.8 on 2023-12-04 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('important', 'Important'), ('normal', 'Normal')], default='normal', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='parent_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dependencies', to='Task.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Task.employee'),
        ),
    ]

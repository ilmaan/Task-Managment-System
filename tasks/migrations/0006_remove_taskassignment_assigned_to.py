# Generated by Django 5.1 on 2024-08-22 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassignment',
            name='assigned_to',
        ),
    ]

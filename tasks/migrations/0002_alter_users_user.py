# Generated by Django 5.1 on 2024-08-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

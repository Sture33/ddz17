# Generated by Django 5.0 on 2023-12-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app17', '0003_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='in process', max_length=255),
        ),
    ]

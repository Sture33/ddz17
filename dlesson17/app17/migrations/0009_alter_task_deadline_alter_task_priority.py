# Generated by Django 5.0 on 2024-01-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app17', '0008_actions_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('red', 'высокий'), ('yellow', 'средний'), ('blue', 'низкий')], max_length=255),
        ),
    ]
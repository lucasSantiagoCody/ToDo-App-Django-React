# Generated by Django 5.0.3 on 2024-04-06 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 23, 18, 37, 658458)),
        ),
    ]

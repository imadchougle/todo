# Generated by Django 4.2.7 on 2023-12-01 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
    ]
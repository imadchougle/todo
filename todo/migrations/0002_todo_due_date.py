# Generated by Django 4.2.7 on 2023-12-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
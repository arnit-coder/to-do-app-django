# Generated by Django 3.2.13 on 2022-08-04 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['task_status']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='Time_posted',
        ),
    ]
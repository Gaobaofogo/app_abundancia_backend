# Generated by Django 2.1.7 on 2019-03-17 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tasklog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklog',
            old_name='id_task',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='tasklog',
            old_name='id_user',
            new_name='user',
        ),
    ]

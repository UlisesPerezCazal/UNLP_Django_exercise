# Generated by Django 4.0 on 2021-12-29 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course_student',
            new_name='Enrol',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]

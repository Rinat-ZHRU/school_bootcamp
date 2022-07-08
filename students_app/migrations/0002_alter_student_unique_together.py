# Generated by Django 4.0.6 on 2022-07-07 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_alter_course_options_alter_course_name'),
        ('students_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender')},
        ),
    ]

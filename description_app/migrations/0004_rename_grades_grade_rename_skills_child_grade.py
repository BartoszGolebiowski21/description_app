# Generated by Django 4.2.6 on 2023-10-26 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('description_app', '0003_grades_description_child_skills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='skills',
            new_name='grade',
        ),
    ]

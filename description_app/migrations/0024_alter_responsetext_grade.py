# Generated by Django 4.2.6 on 2023-10-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('description_app', '0023_alter_childskill_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsetext',
            name='grade',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2)], max_length=1, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-27 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('description_app', '0021_responsetext_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childskill',
            name='grade',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]

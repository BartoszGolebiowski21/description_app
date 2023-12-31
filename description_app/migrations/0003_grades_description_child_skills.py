# Generated by Django 4.2.6 on 2023-10-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('description_app', '0002_rename_pupil_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czytanie', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=6)),
                ('pisanie', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=6)),
                ('liczenie', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='description_app.child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='skills',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='description_app.grades'),
        ),
    ]

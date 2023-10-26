# Generated by Django 4.2.6 on 2023-10-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('description_app', '0005_remove_child_grade_grade_child_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], max_length=1)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('chłopiec', 'chłopiec'), ('dziewczynka', 'dziewczynka')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.AddField(
            model_name='skill',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='description_app.child'),
        ),
    ]

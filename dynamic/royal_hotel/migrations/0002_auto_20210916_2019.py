# Generated by Django 3.2.7 on 2021-09-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royal_hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='f_content',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='g_content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='s_content',
            field=models.TextField(max_length=500),
        ),
    ]

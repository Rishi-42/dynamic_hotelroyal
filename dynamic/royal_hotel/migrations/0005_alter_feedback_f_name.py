# Generated by Django 3.2.7 on 2021-09-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royal_hotel', '0004_alter_feedback_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='f_name',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 2.1.2 on 2018-11-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0018_auto_20181101_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
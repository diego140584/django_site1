# Generated by Django 2.1.2 on 2018-10-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0003_auto_20181010_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Wed Oct 10 15:05:50 2018'),
        ),
    ]
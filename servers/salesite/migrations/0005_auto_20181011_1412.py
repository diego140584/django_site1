# Generated by Django 2.1.2 on 2018-10-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0004_auto_20181010_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Thu Oct 11 14:12:36 2018'),
        ),
        migrations.AlterField(
            model_name='server',
            name='description',
            field=models.TextField(max_length=120, null=True),
        ),
    ]

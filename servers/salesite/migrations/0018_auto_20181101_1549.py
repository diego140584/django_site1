# Generated by Django 2.1.2 on 2018-11-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0017_auto_20181101_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pc',
            name='model_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='server',
            name='model_name',
            field=models.CharField(max_length=64),
        ),
    ]

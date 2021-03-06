# Generated by Django 2.1.2 on 2018-10-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0010_auto_20181024_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_registration',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=64),
        ),
        migrations.AlterField(
            model_name='customer',
            name='firm',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='customer',
            name='role',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Tue Oct 30 12:12:33 2018'),
        ),
    ]

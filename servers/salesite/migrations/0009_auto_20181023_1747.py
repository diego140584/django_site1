# Generated by Django 2.1.2 on 2018-10-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0008_auto_20181023_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contact',
            new_name='firm',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_registration',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Tue Oct 23 17:47:21 2018'),
        ),
    ]

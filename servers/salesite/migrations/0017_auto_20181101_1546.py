# Generated by Django 2.1.2 on 2018-11-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesite', '0016_auto_20181030_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='model_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salesite.Customer'),
        ),
    ]